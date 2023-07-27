import nextcord
from nextcord.ext import commands
from dice import d4, d6, d8, d10, d12, d20, d100

intents = nextcord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!',intents=intents)


@client.event
async def on_ready():
    print("Bot pronto para uso hehe")
    print("------------------------")
    
    
@client.command()
async def oi(ctx):
    await ctx.send("Oi tudo bem? Sou um bot para rpg :)")


testServerId=1133139602992017409    
@client.slash_command(name = "rolar", description="Rolagem de d4, d6, d8, d12, d20 e d100", guild_ids=[testServerId])    
async def roll(interaction: nextcord.Interaction, dado:str):    
    
    quantidade, dTipo = dado.split('d')
    quantidade = int(quantidade)
    dTipo = "d" + dTipo
    
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
    
    await interaction.response.send_message(f"{interaction.user.mention} :game_die: Rolou um {dado} e tirou {resultado}")


##    
    
client.run('MTEzMzA0MTAwNDI3MDg1MDE1Mw.G2mc0l.INBPBa8f5xPWJqQxVrbtlUsUq4QkH-CbVwXtYE')
