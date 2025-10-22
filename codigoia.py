import discord
from discord.ext import commands
from Angel.pan import analize_THIS
from ia_detect_animal.pan import Que_animal_seraaa
from codigoGPT import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

true, false = True, False
"👍👍👍👍👍👍"

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def analiza_algo(ctx):
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        
        await attachment.save(attachment.filename)
        
        await ctx.send(analize_THIS(attachment.filename))
    else:
        await ctx.send("pon una imagen D:<")

@bot.command()
async def Que_animal_sera(ctx):
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        
        await attachment.save(attachment.filename)
        
        await ctx.send(Que_animal_seraaa(attachment.filename))
    else:
        await ctx.send("pon una imagen D:<")

@bot.command()
async def Pipu_ai(ctx, que_dijo="El chistosito que llamo este comando y me desperdicio un token de gemini no puso nada."):
    who_this = ctx.author
    try:
        await ctx.send(responde_gemini(str(que_dijo), str(who_this)))
    except:
        await ctx.send('Ni idea. \n Solo entiendo cosas entre comillas \n Como esto: ($Pipu_ai "Hola como estas")')
hyper_secret_token = open("../cloro.txt", 'r')

bot.run(hyper_secret_token.read())
#hola
#chao :p