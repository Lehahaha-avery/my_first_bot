import discord
from discord.ext import commands
from settings import settings
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    
@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def ruletka(ctx):
    flip = random.randint(1 , 9)
    frazi = ["Вам повезло, патрона не было", "Фух, пронесло, пусто", "ЛЕГЧАЙШАЯ, ПАТРОНА НЕТУ", "а вы везучий, остались живы(это временно)"]
    if flip == 1:
        await ctx.send("Смерти")
    else:
        await ctx.send(random.choice(frazi))




bot.run(settings["TOKEN"])
