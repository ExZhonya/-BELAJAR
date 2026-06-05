from discord.ext import commands
import discord

class help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def Help(self,ctx):
        embed = discord.Embed(
            title="Help Commands",
            description="List of all Commands.",
            color=discord.Color.blue()
        )
        embed.add_field(name="Field 1", value="First Field Value", inline=False)
        embed.add_field(name="Field 2", value="Second Field Value", inline=False)

        embed.set_footer(text="This is a Footer bish.")
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(help(bot))