import discord
from discord.ext import commands
from Angel.pan import analize_THIS
from ia_detect_animal.pan import Que_animal_seraaa
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

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
        "pon una imagen D:<"
@bot.command()
async def Que_animal_sera(ctx):
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        
        await attachment.save(attachment.filename)
        
        await ctx.send(Que_animal_seraaa(attachment.filename))
    else:
        "pon una imagen D:<"

hyper_secret_token = open("/home/angel/Documents/algo/cloro.txt", 'r')
bot.run(hyper_secret_token.read())
#hola