import discord
from discord.ext import commands
from bot_recicle_logic import dicas_function
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)



@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def recicle(ctx):
    await ctx.send(dicas_function())
bot.run("token")
