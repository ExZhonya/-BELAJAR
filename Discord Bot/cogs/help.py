from discord.ext import commands
import discord

class help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(aliases=['cmd'])
    async def help(self,ctx):
        embed = discord.Embed(
            title="Help Commands",
            description="List of all Commands.",
            color=discord.Color.blue()
        )
        embed.add_field(name="!Help | !cmd", value="To see lists of every commands of this bot.", inline=False)
        embed.add_field(name="!Purge | !delete", value="To delete any amounts of messages in the channel.", inline=False)
        embed.add_field(name="!Kick", value="To kick any users.", inline=False)
        embed.add_field(name="!Ban", value="To Ban any users.", inline=False)

        embed.set_footer(text="Last updated: 8/29/2026")
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(help(bot))