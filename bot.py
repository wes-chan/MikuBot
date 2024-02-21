import os
import discord

from dotenv import load_dotenv, dotenv_values
load_dotenv()


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Test
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')





# Run the Bot

client.run(os.getenv("TOKEN"))