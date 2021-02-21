import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
# helper function that returns a category ID given a category's name and message it was in
def getCatIDbyName(message, name):
    for cat in message.guild.categories:
        if cat.name.lower() == name.lower():
            return cat.id
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    channels = message.channel_mentions
    if len(channels) != 0:
        teamdev = getCatIDbyName(message, "Teams Discussion")
        for ch in channels:
            if ch.category.id == teamdev:
                mention = ch.changed_roles[0].mention
                botmsg = "Hi "+ mention +"! "+ message.author.name + " (user " + message.author.mention +") from " +message.channel.name +" says \"" + message.content +"\"" 
                await ch.send(botmsg)  
client.run(TOKEN)