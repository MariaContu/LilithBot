import discord
from discord.ext import commands
from dice import *

client = commands.Bot(command_prefix='!',intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Bot pronto para uso hehe")
    print("------------------------")
    
    
@client.command()
async def oizinho(ctx):
    await ctx.send("Oi tudo bem? Sou um bot para rpg :)")

client.run('MTEzMzA0MTAwNDI3MDg1MDE1Mw.G2mc0l.INBPBa8f5xPWJqQxVrbtlUsUq4QkH-CbVwXtYE')

@client.command()
async def rolar(ctx,dado:str):
    dados_disponiveis = ["d4", "d8", "d10", "d12", "d20", "d100"]
    resultado = None
    if dado == "d4":
        resultado = d4()
    elif dado == "d8":
        resultado = d8()
    elif dado == "d10":
        resultado = d10()
    elif dado == "d12":
        resultado = d12()
    elif dado == "d20":
        resultado = d20()
    elif dado == "d100":
        resultado = d100()

    await ctx.send(resultado)