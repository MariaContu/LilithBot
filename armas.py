class Armas:
    def __init__(self,arma,cat,dano,crit,alcance,tipo,espaco):
        self.arma=arma
        self.cat=cat
        self.dano=dano
        self.dano=dano
        self.crit=crit
        self.alcance=alcance
        self.tipo=tipo
        self.espaco=espaco
    
class ArmasSimples(Armas):
    def __init__(self, arma, cat, dano, crit, alcance, tipo, espaco):
        super().__init__(arma, cat, dano, crit, alcance, tipo, espaco)
        
class ArmasPesadas(Armas):
    def __init__(self, arma, cat, dano, crit, alcance, tipo, espaco):
        super().__init__(arma, cat, dano, crit, alcance, tipo, espaco)
        
class ArmasTaticas(Armas):
    def __init__(self, arma, cat, dano, crit, alcance, tipo, espaco):
        super().__init__(arma, cat, dano, crit, alcance, tipo, espaco)