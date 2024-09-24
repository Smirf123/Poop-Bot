import discord
from discord.ext import commands

TOKEN = "ODc2NjIyODE0MDI1NzY0ODk1.G_adfc.FITOR2mMaHpc8kVZWairwMFZDf9isJKesfsJYE"
activity = discord.Activity(type=discord.ActivityType.watching, name="for your messages")
client = commands.Bot(command_prefix = "}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        await message.channel.send(":shit:")


client.run(TOKEN)
ODc2NjIyODE0MDI1NzY0ODk1.GpiTM_.3JOU6etzcuB4fisIFJksSHpL_NqUIsnwKUSafI
ODc2NjIyODE0MDI1NzY0ODk1.GZfkp_.o2JBlNzG8ME04snOGQXAT__Q28DdYTqUQ0lmGE
