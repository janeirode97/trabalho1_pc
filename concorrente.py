# Código Concorrente

from threading import Thread
import time
import ast, requests
import statistics

url = "https://roll-dice1.p.rapidapi.com/rollDice"

headers = {
 "X-RapidAPI-Key": "a44cc2d6eamsh001776fcf6f38c3p17d986jsn1a82ecf22f6d",
 "X-RapidAPI-Host": "roll-dice1.p.rapidapi.com"
}


class Th(Thread):

	def __init__(self):
		Thread.__init__(self)

	def run(self):
		self.num = ast.literal_eval(
		 requests.request("GET", url, headers=headers).text)["data"]["Dice"]


def Versao_Concorrente(num_req):
	inicio = time.time()
	lista_threads = []
	for thread in range(num_req):
		lista_threads.append(Th())
	for thread in lista_threads:
		thread.start()
	fim = time.time()
	return fim - inicio


def Testar_Concorrente(list_num_req):
	resultados = {}
	for num_req in list_num_req:
		resultados[f"{num_req}_req"] = []
		for _ in range(20):
			tempo_concorrente = Versao_Concorrente(num_req)
			resultados[f"{num_req}_req"].append(tempo_concorrente)
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


resultado_concorrente = Testar_Concorrente([2, 4, 8])
estatistica_concorrente = Estatisticas(resultado_concorrente)
print(estatistica_concorrente)


