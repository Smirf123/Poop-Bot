import discord
from discord.ext import commands

TOKEN = "NzgyMDU1OTQ0NjkwNzI4OTcw.X8GoWw.kTC4BrYCtfQQrWh2X4kJnSAXXVY"
activity = discord.Activity(type=discord.ActivityType.watching, name="for your messages")
client = commands.Bot(command_prefix = "}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        await message.channel.send(":shit:")


client.run(TOKEN)