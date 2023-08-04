from pericias import Pericia, Acrobacia,Adestramento,Artes,Atletismo,Atualidades,Ciencias,Crime,Diplomacia,Enganacao,Fortitude,Furtividade,Iniciativa,Intimidacao,Intuicao,Investigacao,Luta,Medicina,Ocultismo,Percepcao,Pilotagem,Pontaria,Profissao,Reflexos,Religiao,Sobrevivencia,Tatica,Tecnologia,Vontade

class Origens():
    def __init__(self,nome,poder,pericias=[]):
        self.nome=nome
        self.pericias=pericias
        self.poder=poder
        
##### ORIGENS DO SISTEMA DE ORDEM #####

Academico=Origens("Academico","**Saber é Poder**",[Ciencias,Investigacao])
AgenteDeSaude=Origens("Agente De Saude","**Tecnica Medicinal**",[Intuicao,Medicina])
Amnesico=Origens("Amnesico","**Vislumbres do Passado**",["2 a Escolha do Mestre"])
Artista=Origens("Artista", "**Magnum Opus**",[Artes,Enganacao])
Atleta=Origens("Atleta","**110%**",[Acrobacia,Atletismo])
Chef=Origens("Chef","**Ingrediente Secreto**",[Fortitude,Profissao])
Criminoso=Origens("Criminoso", "**O Crime Compensa**",[Crime,Furtividade])
CultistaArrependido=Origens("Cultista Arrependido","**Traços do Outro Lado**",[Ocultismo,Religiao])
Desgarrado=Origens("Desgarrado","**Calejado**",[Fortitude,Sobrevivencia])
Engenheiro=Origens("Engenheiro","**Ferramentas Favoritas**",[Profissao,Tecnologia])
Executivo=Origens("Executivo","**Processo Otimizado**",[Diplomacia,Profissao])
Investigador=Origens("Investigador","**Faro para Pistas",[Investigacao,Percepcao])
Lutador=Origens("Lutador","**Mão Pesada**",[Luta,Reflexos])
Magnata=Origens("Magnata","**Patrocinador da Ordem**",[Diplomacia,Pilotagem])
Mercenario=Origens("Mercenario","**Posição de Combate**",[Iniciativa,Intimidacao])
Militar=Origens("Militar","**Para Bellum**",[Pontaria,Tatica])
Operario=Origens("Operario","**Ferramenta de Trabalho**",[Fortitude,Profissao])
Policial=Origens("Policial","**Patrulha**",[Percepcao,Pontaria])
Religioso=Origens("Religioso","**Acalentar**",[Religiao,Vontade])
ServidorPublico=Origens("Servidor Publico","**Espirito Civico**",[Intuicao,Vontade])
TeoricoDaConspiracao=Origens("Teorico da Conspiração","**Eu Ja Sabia**",[Investigacao,Ocultismo])
TI=Origens("TI","**Motor de Busca**",[Tecnologia,Investigacao])
TrabalhadorRural=Origens("Trabalhador Rural","**Desbravador**",[Adestramento,Sobrevivencia])
Trambiqueiro=Origens("Trambiqueiro","**Impostor**",[Crime,Enganacao])
Universitario=Origens("Universitario","**Dedicação**",[Atualidades,Investigacao])
Vitima=Origens("Vitima","**Cicatrizes Psicologicas**",[Reflexos,Vontade])