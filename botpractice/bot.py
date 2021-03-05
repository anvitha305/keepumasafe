import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
# loads our environment variables - stuff we can't post on GitHub
load_dotenv()


intents = discord.Intents.default()
intents.members = True

# info you need to connect the bot to Discord
TOKEN = os.getenv('DISCORD_TOKEN')
client =  commands.Bot(command_prefix='/', intents=intents)


@client.event
async def on_ready():
    client.load_extension("itc")
    client.load_extension("welcog")
    print("ready")

# important - actually connects our bot to Discord so it can work its magic
client.run(TOKEN)
