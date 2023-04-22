from discord.ext import commands
# import ../database/db.py
from database import db
# import db controller
from database import db_controller
# import Time module
from datetime import datetime
# import helpers
from helpers import check_time

# Descriptions for all commands
help = {
    "register": "Register your account to the mudae clon bot",
    "spin": "Obtain a character using a free spin"
}


class Mudae(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.database = db.get_connection()

    @commands.command(help=help["register"])
    async def register(self, ctx):
        new_user = {
            "discord_id": str(ctx.author.id),
            "coins": 50,
            "last_spin": "available",
            "own_characters": [],
        }
        collection = self.database["users"]
        if (collection.find_one({"discord_id": str(ctx.author.id)})):
            return await ctx.message.reply("You are already registered.")
        else:
            try:
                collection.insert_one(new_user)
                return await ctx.message.reply("You have successfully registered.")
            except Exception as e:
                # error handler no olvidar
                return await ctx.message.reply("An error has occurred, please try again later.")

    @commands.command(help=help["spin"])
    async def spin(self, ctx):
        collection = self.database["users"]
        user_doc = collection.find_one({"discord_id": str(ctx.author.id)})
        if not (user_doc):
            return await ctx.message.reply("You're not registered. use !register")
        else:
            # Get actual time
            now = datetime.now()
            actual_time = now.strftime("%d/%m/%Y/%H:%M")
            # flow control
            if (user_doc["last_spin"] == "available"):
                resultado = db_controller.updateUser(
                    str(actual_time), str(ctx.author.id))
                return await ctx.message.reply("Congratulations, you got this character: not finished yet")
            else:
                # Calculate the time that has elapsed since the last free spin
                difference_min = check_time.getDifference(
                    user_doc["last_spin"], actual_time)
                # If the difference > 30 minutes, then give a free spin.
                if (difference_min > 2):
                    resultado = db_controller.updateUser(
                        str(actual_time), str(ctx.author.id))
                    return await ctx.message.reply("Congratulations, you got this character: not finished yet")
                # else do nothing
                else:
                    return await ctx.message.reply("You don't have a free spin")


async def setup(bot):
    await bot.add_cog(Mudae(bot))
