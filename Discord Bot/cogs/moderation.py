from discord.ext import commands
from datetime import timedelta
import discord
import re

# ===============DURATION===============
DURATION_RE = re.compile(r"(\d+)([smhd])")
UNITS = {"s": "seconds", "m": "minutes", "h": "hours", "d": "days"}
def parse_duration(duration: str) -> timedelta | None:
    matches = DURATION_RE.findall(duration.lower())
    if not matches:
        return None
    kwargs = {}
    for amount, unit in matches:
        key = UNITS[unit]
        kwargs[key] = kwargs.get(key, 0) + int(amount)
    return timedelta(**kwargs)
# ===============DM MEMBER===============
async def notify_member(member: discord.Member, guild: discord.Guild, action: str, reason=None, duration=None):
    text = f"You have been **{action}** in **{guild.name}** ({guild.id})."
    if duration:
        text += f"\nDuration: {duration}"
    text += f"\nReason: {reason}" if reason else "\nReason: No reason provided."

    try:
        await member.send(text)
        return True
    except (discord.Forbidden, discord.HTTPException):
        return False

def check_hierarchy(ctx: commands.Context, member: discord.Member) -> str | None:
    if member == ctx.author:
        return "You can't do that to yourself gng"
    if member == ctx.guild.me:
        return "Nuh uh, don't do that to me you brat."
    if member == ctx.guild.owner:
        return "Wow gng, to the owner? seriously? crazy. Nuh Uh."
    if ctx.author != ctx.guild.owner and member.top_role >= ctx.author.top_role:
        return "I can't do that gng. They're more powerful than you!(Higher or equal role.)"
    if member.top_role >= ctx.guild.me.top_role:
        return "I can't do that gng. They're more powerful than mine!(Higher or equal role.)"
    return None
# =============================================

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="purge", aliases=["clear", "delete"])
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int = 0):
        if amount < 1:
            msg = await ctx.send("Please give a number greater than 0.")
            await msg.delete(delay=3)
            return
        amount = min(amount, 100)  # 100 as safety cap

        deleted = await ctx.channel.purge(limit=amount + 1)
        result = await ctx.send(f"Deleted {len(deleted) - 1} messages.")
        await result.delete(delay=5)

    @commands.command(name="kick")
    @commands.bot_has_permissions(kick_members=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        error = check_hierarchy(ctx, member)
        if error:
            await ctx.message.delete()
            msg = await ctx.send(error)
            await msg.delete(delay=5)
            return

        await ctx.message.delete()
        sent = await notify_member(member, ctx.guild, "kicked", reason=reason)
        await member.kick(reason=reason)

        text = f"{member.mention} has been kicked."
        if reason:
            text += f"\nReason: {reason}"
        if not sent:
            text += "\n*(Could not DM this user.)*"
        msg = await ctx.send(text)
        await msg.delete(delay=5)

    @commands.command(name="ban")
    @commands.bot_has_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        error = check_hierarchy(ctx, member)
        if error:
            await ctx.message.delete()
            msg = await ctx.send(error)
            await msg.delete(delay=3)
            return

        await ctx.message.delete()
        sent = await notify_member(member, ctx.guild, "banned", reason=reason)
        await member.ban(reason=reason)

        text = f"{member.mention} ({member.id}) has been banned."
        if reason:
            text += f"\nReason: {reason}"
        if not sent:
            text += "\n*(Could not DM this user.)*"
        msg = await ctx.send(text)
        await msg.delete(delay=5)

    @commands.command(name="unban")
    @commands.bot_has_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: discord.User, *, reason=None):
        await ctx.message.delete()
        await ctx.guild.unban(member, reason=reason)
        text = f"{member} ({member.id}) has been unbanned"
        if reason:
            text += f"\nReason: {reason}"
        msg = await ctx.send(text)
        await msg.delete(delay=5)

    @commands.command(name="timeout", aliases=["mute"])
    @commands.bot_has_permissions(moderate_members=True)
    @commands.has_permissions(moderate_members=True)
    async def timeout(self, ctx, member: discord.Member, duration: str = "15m", *, reason=None):
        error = check_hierarchy(ctx, member)
        if error:
            await ctx.message.delete()
            msg = await ctx.send(error)
            await msg.delete(delay=5)
            return

        delta = parse_duration(duration)
        if delta is None:
            msg = await ctx.send("Invalid Duration!. Please use something like `10m`, `1h`, `2d`, `1h30m`.")
            await msg.delete(delay=5)
            return

        if delta > timedelta(days=28):
            msg = await ctx.send("Timeout duration cannot exceed 28 days!.")
            await msg.delete(delay=5)
            return

        await ctx.message.delete()
        sent = await notify_member(member, ctx.guild, "timed out", reason=reason, duration=duration)
        await member.timeout(delta, reason=reason)

        text = f"{member.mention}({member.id}) has been timed out for {duration}."
        if reason:
            text += f"\nReason: {reason}"
        if not sent:
            text += "\n*(Could not DM this user.)*"
        msg = await ctx.send(text)
        await msg.delete(delay=5)

    @commands.command(name="untimeout", aliases=["unmute"])
    @commands.bot_has_permissions(moderate_members=True)
    @commands.has_permissions(moderate_members=True)
    async def untimeout(self, ctx, member: discord.Member):
        await ctx.message.delete()
        await member.timeout(None)
        msg = await ctx.send(f"{member.mention}({member.id}) has been unmuted.")
        await msg.delete(delay=3)


async def setup(bot):
    await bot.add_cog(Mod(bot))