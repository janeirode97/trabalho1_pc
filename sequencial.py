# Código sequencial

import time
import ast, requests
import statistics

url = "https://roll-dice1.p.rapidapi.com/rollDice"

headers = {
 "X-RapidAPI-Key": "a44cc2d6eamsh001776fcf6f38c3p17d986jsn1a82ecf22f6d",
 "X-RapidAPI-Host": "roll-dice1.p.rapidapi.com"
}

def Versao_Sequencial(num_req):
	inicio = time.time()

	for req in range(num_req):
		num = ast.literal_eval(requests.request(
		 "GET", url, headers=headers).text)["data"]["Dice"]
	fim = time.time()
	return fim - inicio



def Testar_Sequencial(list_num_req):
	resultados = {}
	for num_req in list_num_req:
		resultados[f"{num_req}_req"] = []
		for _ in range(20):
			tempo_sequencial = Versao_Sequencial(num_req)
			resultados[f"{num_req}_req"].append(tempo_sequencial)
	return resultados


def Estatisticas(dicionario):
	estatisticas = {}
	for chave in dicionario.keys():
		estatisticas[chave] = {}
		estatisticas[chave]["valor_maximo"] = max(dicionario[chave])
		estatisticas[chave]["valor_minimo"] = min(dicionario[chave])
		estatisticas[chave]["media_aritmetica"] = statistics.mean(dicionario[chave])
		estatisticas[chave]["desvio_padrao"] = statistics.stdev(dicionario[chave])
	return estatisticas

resultado_sequencial = Testar_Sequencial([2, 4, 8])
estatistica_sequencial = Estatisticas(resultado_sequencial)
print(estatistica_sequencial)

