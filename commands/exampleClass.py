import discord
from discord.ext import commands


class Example_class(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def example_command(self, ctx):
        await ctx.reply("example command")


async def setup(bot):
    await bot.add_cog(Example_class(bot))
