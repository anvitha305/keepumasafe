import os
import discord
from discord.ext import commands

# helper function that returns a category ID given a category's name and message it was in
def getCatIDbyName(message, name):
    return discord.utils.find(lambda cat: cat.name.lower() == name.lower(),message.guild.categories).id

# helper function to get a team's corresponding @ mention given the channel name and guild/server
# returns None if there is no role (keeps anonymity of private channels)
def atMention(guild, ch_name):
    roleName = ch_name.replace("&","and").replace("press-and-","").replace("-", " ").title()
    for rol in guild.roles:
        if rol.name == roleName:
            return rol.mention
    return None

class ITC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # registers the event our bot is listening for
    @commands.Cog.listener()
    # does this whenever a message is sent on the server
    async def on_message(self, message):
        # paramount to ensure the bot doesn't keep responding to itself when it uses the channel referencing feature
        if message.author == self.bot.user:
            return
        channels = message.channel_mentions
        # only executes our code if it contains references to channels
        if len(channels) != 0:
            # checks if the message was sent in one of the Teams Discussion channels
            teamdev = getCatIDbyName(message, "Teams Discussion")
            # ensures bot does the loop stuff for every channel being referenced in the message
            for ch in channels:
                # makes sure the channel being referred to is also one of the Teams Discussion channels
                if ch.category.id == teamdev:
                    # gets appropriate @ mention for the roles associated with each team - not for private channels
                    mention = atMention(message.guild, ch.name)
                    if mention is not None:
                        # creates and sends the"relaying" message in the referenced channel
                        botmsg = "Hi "+ mention +"! "+ message.author.name + " (user " + message.author.mention +") from " +message.channel.mention +" says \"" + message.content +"\"" 
                        await ch.send(botmsg)  
def setup(bot):
    bot.add_cog(ITC(bot))
