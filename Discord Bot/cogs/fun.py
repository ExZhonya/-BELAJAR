from discord.ext import commands
import time

class fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        message = await ctx.send("Pong!")
        ping = round(self.bot.latency * 1000)
        await message.edit(content=f"Pong!\n`Latency:{ping}ms`")

class easter_egg(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ilovemedine(self,ctx):
        await ctx.message.delete()
        await ctx.send("I LOVE MEEDDDIIINNEEEEE!!!!!!!!!")


async def setup(bot):
    await bot.add_cog(fun(bot))
    await bot.add_cog(easter_egg(bot))