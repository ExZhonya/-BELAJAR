from discord.ext import commands


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            msg = await ctx.send("Command not recognized. Try `!help` to see the list of commands.")
            await msg.delete(delay=3)
            await ctx.message.delete(delay=3)

        elif isinstance(error, commands.MissingRequiredArgument):
            msg = await ctx.send(f"Missing argument: `{error.param.name}`!")
            await msg.delete(delay=3)
            await ctx.message.delete(delay=3)

        elif isinstance(error, commands.MemberNotFound):
            msg = await ctx.send("Member not found!")
            await msg.delete(delay=3)
            await ctx.message.delete(delay=3)

        elif isinstance(error, commands.MissingPermissions):
            msg = await ctx.send("You don't have permission to use that command.")
            await msg.delete(delay=3)
            await ctx.message.delete(delay=3)

        elif isinstance(error, commands.BotMissingPermissions):
            msg = await ctx.send("I don't have the permissions needed to do that.")
            await msg.delete(delay=3)
            await ctx.message.delete()

        elif isinstance(error, TypeError):
            msg = await ctx.send("TypeError! Something went wrong.")
            await msg.delete(delay=3)
            await ctx.message.delete()

        else:
            msg = await ctx.send("Unknown Error. Please contact the owner(`exzhonya`).")
            await msg.delete(delay=5)
            await ctx.message.delete()
            raise error
            


async def setup(bot):
    await bot.add_cog(ErrorHandler(bot))