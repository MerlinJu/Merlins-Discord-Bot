import discord

@bot.command()
async def repeat_user(context, arg):
    await context.send(arg)