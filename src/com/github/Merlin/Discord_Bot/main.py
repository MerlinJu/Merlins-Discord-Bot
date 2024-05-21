import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from typing import Final

# load the .env file 
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')


# define the intents for the bot
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

# set the command prefix to !, then set the intents to the predefined intents
bot = commands.Bot(command_prefix="!", intents=intents)


# Error handling for invalid commands
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandError):
        await ctx.send('Command not found. Please check the command and try again.')

# event when the bot is ready 
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


# repeat the message that was send to the bot as a command
@bot.command()
async def repeat_user(ctx, arg):
    await ctx.send(arg)

# print the current channel name
@bot.command(name="channel")
async def print_channel(ctx):
    await ctx.send(f'You are in #{ctx.channel}')



# Start the bot if script is manually run
if __name__ == '__main__':
    if TOKEN:
        bot.run(TOKEN)
    else:
        print('Discord Token not found')