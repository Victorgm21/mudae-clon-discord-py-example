import discord
from discord.ext import commands
# import BD
from database.db import mongo_atlas_db
# helpers
from helpers.validators import check_url


class mudae_admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.database = mongo_atlas_db

    @commands.command()
    async def saludar1(self, ctx):
        await ctx.reply("TE ESTOY SALUDANDO")

    @commands.command()
    @commands.has_any_role('admin', 'moderador')
    async def add_character(self, ctx, name, lastname, img_url):
        if (check_url(img_url)):
          new_character = {
              "name": (name + " " + lastname),
              "img": img_url,
          }
          try:
              self.database["characters"].insert_one(new_character)
              # EMBED
              embed = discord.Embed(
                  title="Personaje agregado.", description=f"Ha agregado a {name} a la base de datos correctamente", colour=discord.Colour.red())
              embed.set_image(url=img_url)
              # FIN EMBED
              await ctx.reply(embed = embed)
          except Exception as e:
              print(e)
              await ctx.reply("Ha ocurrido un error")
        else:
          await ctx.reply("Introduzca una URL valida")  


async def setup(bot):
    await bot.add_cog(mudae_admin(bot))
