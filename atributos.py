class Atributos():
    def __init__(self,tipo:str,abrev:str,valor:int):
        self.tipo=tipo
        self.abrev=abrev
        self.valor=valor
        
    def setValor(self,novoValor):
        self.valor=novoValor     

##############    CRIA ATRIBUTOS EXISTENTES    ##############
        
Inteligencia = Atributos("Intelecto","INT",0)
Agilidade = Atributos("Agilidade","AGI",0)
Forca = Atributos("Forca","FOR",0)
Presenca = Atributos("Presenca","PRE",0)
Vigor = Atributos("Vigor","VIG",0)
