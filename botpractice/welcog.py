import os
import discord
from discord.ext import commands

# :thumbsup: for supporter, :art: for art and actions, :satellite: for communications, and :microphone2: for press
rxn_role = {"\U0001f44d": "Supporter", "\U0001f3a8":"Art & Action", "\U0001f4e1":"Communications", "\U0001f399":"Outreach"}
class Welcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # registers the event our bot is listening for
    @commands.Cog.listener()
    # does this whenever a message is sent on the server
    async def on_member_join(self, member):
        guild = member.guild
        ch = discord.utils.find(lambda c: c.name.lower() == 'general', guild.channels)
        # Welcomes a new user
        botmsg = "Welcome " + member.mention + "!"
        await ch.send(botmsg)
        # Lets the users know about reaction roles and how to use this feature
        botmsg = "Anyone can do this to get roles - react with the corresponding emoji to get the role(s) you want:\n"
        for roles in rxn_role.items():
            botmsg += roles[0] + " for " + roles[1] + "\n"
        await ch.send(botmsg)
    @commands.Cog.listener()
    async def on__raw_reaction_add(self, reaction, user):
        # Listens for the reaction and adds roles accordingly, informing the user that it is done
        if reaction.message.author == self.bot.user and "Anyone can do this to get roles" in reaction.message.content:
            for roles in rxn_role.items():
                rol = discord.utils.find(lambda c: c.name.lower() == roles[1].lower(), user.guild.roles)
                if str(reaction.emoji) == roles[0] and not rol in user.roles:
                    await user.add_roles(rol)
                    botmsg =  user.mention + " is part of the "+ roles[1] + " team. Welcome!"
                    await reaction.message.channel.send(botmsg)
def setup(bot):
    bot.add_cog(Welcog(bot))
