import discord
from discord.ext import commands
from dice import d4, d6, d8, d10, d12, d20, d100
from myToken import token

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!',intents=intents)

dados_disponiveis = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100']

@client.event
async def on_ready():
    print("Bot pronto para uso hehe")
    print("------------------------")
    
    
@client.command()
async def oi(ctx):
    await ctx.send("Oi tudo bem? Sou um bot para rpg :)")


testServerId=1133139602992017409  

@client.tree.command(name = "rolar", description="Rolagem de d4, d6, d8, d12, d20 e d100")    
async def roll(interaction: discord.Interaction, dado:str):  
    
    quantidade, dTipo = dado.split('d')
    if not quantidade: quantidade = "1"
    
    quantidade = int(quantidade)
    dTipo = "d" + dTipo
    
    if dTipo not in dados_disponiveis: await interaction.response.send_message(f"Dado {dTipo} não está entre os dados disponívels, por favor insira um valor válido.")
    
    resultado = None
    if dTipo == "d4":
        resultado = d4()
    elif dTipo == "d6":
        resultado = d6()
    elif dTipo == "d8":
        resultado = d8()
    elif dTipo == "d10":
        resultado = d10()
    elif dTipo == "d12":
        resultado = d12()
    elif dTipo == "d20":
        resultado = d20()
    elif dTipo == "d100":
        resultado = d100()
    
    await interaction.response.send_message(f"{interaction.user.mention} :game_die: Rolou {quantidade}{dTipo} e tirou {resultado}")


##    
    
client.run(token)
