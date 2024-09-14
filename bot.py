import discord
import random 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Conexion exitosa, iniciamos sesion como: {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy el bot {bot.user}!')

@bot.command()
async def risa(ctx, count_heh = 5):
    await ctx.send("ja" * count_heh)

@bot.command()
async def creador(ctx):
    await ctx.send(f'Mi creador fue: 𝐇α𝐝𝐞ȥ ᴳᵒᵈメ!')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} se ha unido a {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        # Intenta separar el número de tiradas (rolls) y el número de caras del dado (limit)
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        # Si no puede separar o convertir correctamente, envía un mensaje de error
        await ctx.send('Format has to be in NdN!')
        return

    # Genera los resultados de las tiradas, donde se tiran 'rolls' dados con 'limit' caras cada uno
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    
    # Envía el resultado de las tiradas como mensaje
    await ctx.send(result)


bot.run("TOKEN")
