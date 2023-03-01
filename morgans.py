import discord
from discord.ext import commands
import time

TOKEN = 'MTA3Mzc3NzEzNDY5NjQwNzA4MA.GjXwku.6I1R624sYzYDcFwplQJOO4N1dbMnHQgGccTLIg'

def sendMessage(message, ch):

    client = discord.Client()
    intents = discord.Intents.default()
    client = commands.Bot(command_prefix="!", intents=intents)

    @client.event
    async def on_ready():  #  Called when internal cache is loaded
        print('Discord sending message ...')
        if ch == 0:
            channel = client.get_channel(1073798714080108554)
        elif ch == 1:
            channel = client.get_channel(1073798776176775249)
        elif ch == 9999:
            channel = client.get_channel(1074726278386683947)
        await channel.send(message)
        await client.close()

    client.run(TOKEN)  # Starts up the bot