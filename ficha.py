#armazena as fichas
from atributos import Atributos

class Ficha:
    def __init__(self, nome, player, origem, classe, NEX, desloc, PV, PE, PS, DEF,pericias=[],atributos=[]):
        self.nome =nome
        self.player=player
        self.origem=origem
        self.classe=classe
        self.NEX=NEX
        self.desloc=desloc
        self.PV=PV
        self.PE=PE
        self.PS=PS
        self.DEF=DEF
        self.pericias=pericias
        self.atributos=atributos
        
        # atributos[0]=agilidade | atributos[1]=forca | atributos[2]=intelecto | atributos[3]=presenca | atributos[4]=vigor
        
        def verificaAtri(self):
            somaVal=0
            for atributo in atributos:
                if atributo<=0: return False
                somaVal+=atributo
            
            return somaVal<=9    
        
    