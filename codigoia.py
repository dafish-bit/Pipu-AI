import discord
from discord.ext import commands
from pan import analize_THIS
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
async def analiza(ctx):
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
  
        await attachment.save(attachment.filename)
        
        await ctx.send(analize_THIS(attachment.filename))
    else:

        await ctx.send('No has adjuntado ninguna imagen. Por favor, usa el comando y adjunta una imagen en el mismo mensaje.')
hyper_secret_token = open("/home/angel/Documents/algo/cloro.txt", 'r')
bot.run(hyper_secret_token.read())
#hola