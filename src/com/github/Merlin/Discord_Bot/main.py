import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from typing import Final

# load the .env file 
load_dotenv()


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


# repaet the message that was send to the bot as a command
@bot.command()
async def repeat_user(context, arg):
    await context.send(arg)


# event when the bot is ready 
@bot.event
async def bot_ready():
    print(f"Logged in as {bot.user.name}")



# RUN THE BOT
bot.run(os.getenv('DISCORD_TOKEN'))