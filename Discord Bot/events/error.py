from discord.ext import commands
import discord
import asyncio

class error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):


        if isinstance(error, commands.CommandNotFound):
            msg = await ctx.send(
                "Commands not recognized. try type `!help` to see list of commands."
            )
            await msg.delete(delay=3)
            await ctx.message.delete(delay=3)


        elif isinstance(error, commands.MissingRequiredArgument):
            missing = error.param.name
            return await ctx.send(f"Missing arguments `{missing}`!")

        else:
            raise error
    
async def setup(bot):
    await bot.add_cog(error(bot))