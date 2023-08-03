#armazena as fichas
from atributos import Atributos

class Ficha:
    def __init__(self, nome, player, atributos, origem, classe, NEX, desloc, PV, PE, PS, DEF,pericias=[]):
        self.nome = nome
        self.player = player
        self.atributos = atributos
        self.origem = origem
        self.classe = classe
        self.NEX = NEX
        self.desloc = desloc
        self.PV = PV
        self.PE = PE
        self.PS = PS
        self.DEF = DEF
        self.pericias = pericias
    
    def verificaAtri(self):
        somaVal = 0
        for atributo in self.atributos:
            somaVal += atributo.valor

            if atributo.valor < 0:
                return False

        return somaVal <= 9