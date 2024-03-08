import os
import discord
import random

from discord import app_commands
from discord.ext import commands

from dotenv import load_dotenv, dotenv_values
load_dotenv()

# Settings
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Variables
client = commands.Bot(command_prefix='/', intents = intents)







# Commands
@client.tree.command(name = "sync")
async def sync(ctx: discord.Interaction):
    await client.tree.sync()
    await ctx.response.send_message(f"Command synced!")


@client.tree.command(name = "love")
async def love(interaction: discord.Interaction, user1: str, user2:str):

    math = random.randint(0,100)

    await interaction.response.send_message(f"{user1} :heart: {user2} : **{math}%**")
    
                      


# Run Bot
@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("~ suki da yo"))


client.run(os.getenv("TOKEN"))