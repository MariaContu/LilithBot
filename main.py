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
    todos = ""
    soma = 0
    maior = 0
    if dTipo == "d4":
        for i in range(quantidade):
            resultado = d4()
            todos += f"{resultado} "
            if (resultado>maior): maior = resultado
            soma += resultado
            
    elif dTipo == "d6":
        for i in range(quantidade):
            resultado = d6()
            todos += f"{resultado} "
            if (resultado>maior): maior = resultado
            soma += resultado
            
    elif dTipo == "d8":
        for i in range(quantidade):
            resultado = d8()
            todos += f"{resultado} "
            if (resultado>maior): maior = resultado
            soma += resultado
        
    elif dTipo == "d10":
        for i in range(quantidade):
            resultado = d10()
            todos += f"{resultado} "
            if (resultado>maior): maior = resultado
            soma += resultado
        
    elif dTipo == "d12":
        for i in range(quantidade):
            resultado = d12()
            todos += f"{resultado} "
            if (resultado>maior): maior = resultado
            soma += resultado
        
    elif dTipo == "d20":
        for i in range(quantidade):
            resultado = d20()
            todos += f"{resultado} "
            if (resultado>maior): maior = resultado
            soma += resultado
        
    elif dTipo == "d100":
        for i in range(quantidade):
            resultado = d100()
            todos += f"{resultado} "
            if (resultado>maior): maior = resultado
            soma += resultado
    
    await interaction.response.send_message(f"{interaction.user.mention} :game_die: Rolou **{quantidade}{dTipo}**. Os valores foram: {todos}. A **soma** de todos é **{soma}** e o **maior** valor foi **{maior}**")


##    
    
client.run(token)
