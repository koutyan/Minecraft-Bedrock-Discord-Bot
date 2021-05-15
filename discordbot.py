# Created by Koutyan.S (https://tech.kosukelab.com/)
# This is main program.

import discord
from discord.ext import tasks
import subprocess
import os
import bot_config

TOKEN = bot_config.DISCORD_TOKEN
CHANNEL_ID = bot_config.DISCORD_CHANNEL_ID

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in done.')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/test':
        await message.channel.send('test message')

@tasks.loop(seconds=1)
async def loop():
    subprocess.call("./login_check.sh")

    if os.stat("./login_check_result").st_size != 0:
        f = open("./login_check_result", 'r')
        data = f.readline()
        channel = client.get_channel(int(CHANNEL_ID))
        await channel.send(data)
        f.close()

loop.start()

client.run(TOKEN)