import discord
from discord.ext import commands
from Angel.pan import analize_THIS
from ia_detect_animal.pan import Que_animal_seraaa
from codigoGPT import *
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

true, false = True, False

engine = create_engine('sqlite:///discord_chat_log.db')  # 2. Base para los modelos declarativos
Base = declarative_base()  # 3. Creación de una sesión para interactuar con la DB
Session = sessionmaker(bind=engine)
db_session = Session()
class User_log_identefier(Base):
    id = Column(Integer, primary_key=True)
    user = Column(String(32), nullable=false)
    log = Column(Integer, nullable=false)
class Chat_log(Base):
    id= Column(Integer, primary_key=true)
    id_chat = Column(Integer, nullable=false)
    question = Column(String(2000), nullable=false)
    answer = Column(String(2000), nullable=false)

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

@bot.command()
async def Pipu_ai(ctx, que_dijo="El chistosito que llamo este comando y me desperdicio un token de gemini no puso nada."):
    await ctx.send(responde_gemini(que_dijo))

hyper_secret_token = open("/home/angel/Documents/algo/cloro.txt", 'r')

bot.run(hyper_secret_token.read())
#hola
#chao :p