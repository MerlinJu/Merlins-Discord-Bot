import discord
import os
import random
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

# remove the default help command
bot.remove_command('help')


# Error handling for invalid commands
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandError):
        await ctx.send('Command not found. Please check the command or type "!help" ')

# event when the bot is ready 
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


# HELP COMMAND
@bot.command(name='help')
async def help_all_commands(ctx):
    # create a embedded message with discord.embed
    embed = discord.Embed(title='Available commands:', color=discord.Color.blue())
    embed.add_field(name="'!repeat <message>'", value='print the following word (no spaces allowed).', inline=False)
    embed.add_field(name="'!channel'", value='print the current channel.', inline=False)
    embed.add_field(name="'!slap <reason>'", value='slap a random person in the server with a reason.', inline=False)
    await ctx.send(embed=embed)


# repeat the message that was send to the bot as a command
@bot.command(name='repeat')
async def repeat_user(ctx, arg):
    await ctx.send(arg)

# print the current channel name
@bot.command(name="channel")
async def print_channel(ctx):
    await ctx.send(f'You are in #{ctx.channel}')


# custom converter class for slapping someone
class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        user_to_be_slapped = random.choice(ctx.guild.members)
        return f'{ctx.author} slapped {user_to_be_slapped} because {argument}' 
    
# slap someone in the discord 
@bot.command(name='slap')
async def slap_random_user(ctx, *, reason: Slapper):
    # reason parameter will be converted into the formatted string as it is expected to be a Slapper object 
    await ctx.send(reason)



# Start the bot if script is manually run
if __name__ == '__main__':
    if TOKEN:
        bot.run(TOKEN)
    else:
        print('Discord Token not found')