from discord.ext import commands
import discord
from discord import TextChannel
from discord.utils import utcnow, format_dt


class general(commands.Cog):

    @commands.command()
    async def serverinfo(self,ctx):
        guild = ctx.guild
        embed = discord.Embed(title=f"Server Info - {guild.name}", color=discord.Color.blue())
        embed.add_field(name="Owner", value=guild.owner, inline=False)
        embed.add_field(name="Created On", value=guild.created_at.strftime("%B %d, %Y"), inline=False)
        embed.add_field(name="Member", value=guild.member_count, inline=False)
        embed.add_field(name="Roles", value=len(guild.roles), inline=False)
        embed.add_field(name="Text Channel", value=len([ch for ch in guild.channels if isinstance(ch, discord.TextChannel)]), inline=True)
        embed.add_field(name="Voice Channel", value=len([ch for ch in guild.channels if isinstance(ch, discord.VoiceChannel)]), inline=True)

        await ctx.send(embed=embed)
    

async def setup(bot):
    await bot.add_cog(general(bot))