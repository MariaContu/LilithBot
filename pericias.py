#pericias.py = coontem as pericias, incluindo nome 

class Pericia:
    def __init__(self,nome,atriBase, treinada=False,penalidadeCarga=False,needKit=False):
        self.nome = nome
        self.atriBase = atriBase
        self.treinada = treinada
        self.penalidadeCarga=penalidadeCarga
        self.needKit=needKit
        
        
##### PERICIAS DO SISTEMA DE ORDEM #####

Acrobacia = Pericia("Acrobacia","Agilidade",penalidadeCarga=True)
Adestramento = Pericia("Adestramento","Presenca",treinada=True)
Artes = Pericia("Artes","Presenca",treinada=True)
Atletismo = Pericia("Atletismo","Forca")
Atualidades = Pericia("Atualidades","Inteligencia")
Ciencias = Pericia("Ciencias","Inteligencia", treinada=True)
Crime = Pericia("Crime","Agilidade",treinada=True,penalidadeCarga=True,needKit=True)
Diplomacia = Pericia("Diplomacia","Presenca")
Enganacao = Pericia("Enganacao","Presenca",needKit=True)
Fortitude = Pericia("Fortitude","Vigor")
Furtividade = Pericia("Furtividade","Agilidade", penalidadeCarga=True)
Iniciativa = Pericia("Iniciativa","Agilidade")
Intimidacao = Pericia("Intimidacao","Presenca")
Intuicao = Pericia("Intuicao","Inteligencia")
Investigacao = Pericia("Investigacao", "Inteligencia")
Luta = Pericia("Luta","Forca")
Medicina = Pericia("Medicina", "Inteligencia", needKit=True)
Ocultismo = Pericia("Ocultismo","Inteligencia",treinada=True)
Percepcao = Pericia("Percepcao","Presenca")
Pilotagem = Pericia("Pilotagem","Agilidade",treinada=True)
Pontaria = Pericia("Pontaria","Agilidade")
Profissao = Pericia("Profissao","Inteligencia",treinada=True)
Reflexos = Pericia("Reflexos","Agilidade")
Religiao = Pericia("Religiao","Presenca",treinada=True)
Sobrevivencia = Pericia("Sobrevivencia","Inteligencia")
Tatica = Pericia("Tatica","Inteligencia",treinada=True)
Tecnologia = Pericia("Tecnologia","Inteligencia",treinada=True,needKit=True)
Vontade = Pericia("Vontade", "Presenca")