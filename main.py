import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!',intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Bot pronto para uso hehe")
    print("------------------------")
    
    
@client.command()
async def oizinho(ctx):
    await ctx.send("Oi tudo bem? Sou um bot para rpg :)")

client.run('MTEzMzA0MTAwNDI3MDg1MDE1Mw.G2mc0l.INBPBa8f5xPWJqQxVrbtlUsUq4QkH-CbVwXtYE')