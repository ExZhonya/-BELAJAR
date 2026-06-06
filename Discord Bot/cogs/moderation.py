from discord.ext import commands
import discord
import asyncio

class purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['purge', 'clear', 'delete'])
    @commands.bot_has_permissions(manage_messages=True)
    async def Purge(self, ctx, amount: int = 0):
        await ctx.channel.purge(limit=amount+1)
        result = await ctx.send(f"Deleted {amount} messages.")
        await result.delete(delay=3)

async def setup(bot):
    await bot.add_cog(purge(bot))
