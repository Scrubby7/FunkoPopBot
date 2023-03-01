import discord

async def send_message(popMessage, channel, client):
    try:
        print('A')
        await channel.send(popMessage)
    except Exception as e:
        print(e)

def run_discord_bot(popMessage, i):
    TOKEN = 'MTA3Mzc3NzEzNDY5NjQwNzA4MA.GjXwku.6I1R624sYzYDcFwplQJOO4N1dbMnHQgGccTLIg'
    print('ENTROU')
    intents = discord.Intents.default()
    #intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print('ENTROUUU')
        if i == 0:
            channel = client.get_channel(1073798714080108554)
        elif i == 1:
            channel = client.get_channel(1073798776176775249)
        elif i == 9999:
            channel = client.get_channel(1074726278386683947)

        await channel.send(popMessage)
        await client.close()

    client.run(TOKEN)