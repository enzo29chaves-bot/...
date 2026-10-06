import discord
from discord.ext import commands
from bot_logic import generador_da_senha
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
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def pasw(ctx):
    await ctx.send(generador_da_senha(10))

@bot.command()
async def like(ctx,arg):
    await ctx.send(arg)
bot.run("")
