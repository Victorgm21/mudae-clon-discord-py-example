import discord
from discord.ext import commands
import pathlib
import settings
import os
from dotenv import load_dotenv


# dotenv variables
load_dotenv()
TOKEN = os.getenv("token")
# intents
intents = discord.Intents.all()
# Directorio donde estan nuestros comandos (Extensiones)
BASE_DIR = pathlib.Path("__file__").parent
COMMANDS_DIR = BASE_DIR / "commands"
# BOT
bot = commands.Bot(command_prefix=settings.PREFIX, intents=intents)


@bot.event
async def on_ready():
    # Cargar archivos de la carpeta "commands"
    for command_file in COMMANDS_DIR.glob("*.py"):
        if command_file.name != "__init__.py":
            await bot.load_extension(f"commands.{command_file.name[:-3]}")
    print("El bot ya esta funcionando!")

bot.run(TOKEN)
