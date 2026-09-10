from discord.ext import commands
import time

class fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        message = await ctx.send("Pong!")
        ping = round(self.bot.latency * 1000)
        await message.edit(content=f"Pong! `Latency:{ping}ms`")

class easter_egg(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ihatemedine(self,ctx):
        await ctx.message.delete()
        msg = await ctx.send("I HATE MEEDDDIIINNEEEEE!!!!!!!!!")
        await msg.delete(delay = 3)

    @commands.command()
    async def zaynamywife(self, ctx):
        await ctx.message.delete()
        msg = await ctx.send("ZAYNA IS MY LOVELY WIFE AND I LOVE HER FOREVER!!!!")
        await msg.delete(delay = 3)


async def setup(bot):
    await bot.add_cog(fun(bot))
    await bot.add_cog(easter_egg(bot))