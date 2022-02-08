import discord
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("token")

client = discord.Client()

@client.event
async def on_ready():
# Print this when the bot starts up for the first time.
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
# Ignore messages from the bot itself so that there's no conflict.
    if message.author == client.user:
        return
# Respond to hello.
    if message.content == 'gm':
        await message.channel.send("Good morning " + str(message.author) + ", you're looking great today!")

client.run(token)