from datetime import datetime
from discord.ext import commands
import discord

from utils.roblox_api import get_user

class Roblox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rblx(self, ctx, *, query):
        msg = await ctx.send(f"Searching `{query}`...")

        user = get_user(query)
        if not user:
            return await msg.edit(content="User not found", embed=None)

        created_dt = datetime.fromisoformat(user["created"].replace("Z", "+00:00"))
        created_unix = int(created_dt.timestamp())
        created_str = f"<t:{created_unix}:D> (<t:{created_unix}:R>)"

        embed = discord.Embed(
            title=f"{user['display']} (@{user['name']})",
            url=f"https://www.roblox.com/users/{user['id']}/profile"
        )
        embed.add_field(name="User ID", value=user["id"])
        embed.add_field(name="Description", value=user['description'], inline=False)
        embed.add_field(name="Created", value=created_str, inline=False)
        embed.set_thumbnail(url=user["avatar"])

        await msg.edit(content=None, embed=embed)

async def setup(bot):
    await bot.add_cog(Roblox(bot))