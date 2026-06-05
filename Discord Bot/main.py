import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

async def load_file():
    print("Loading cogs...")

    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")
            print(f"Loaded: {file}")
    
    for file in os.listdir("./events"):
        if file.endswith(".py"):
            await bot.load_extension(f"events.{file[:-3]}")
            print(f"Loaded: {file}")

    for file in os.listdir("./utils"):
        if file.endswith(".py"):
            await bot.load_extension(f"utils.{file[:-3]}")
            print(f"Loaded: {file}")

    print("All cogs loaded.")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)

async def main():
    async with bot:
        await load_file()
        await bot.start(TOKEN)

asyncio.run(main())