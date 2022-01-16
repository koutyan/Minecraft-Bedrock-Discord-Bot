# Created by Koutyan.S (https://tech.kosukelab.com/)
# This is main program.

import discord
from discord.ext import tasks
import subprocess
import os
import bot_config

TOKEN = bot_config.DISCORD_TOKEN
CHANNEL_ID = bot_config.DISCORD_CHANNEL_ID
CHANNEL_SERVER_ID = bot_config.DISCORD_SERVER_CHANNEL_ID

client = discord.Client()

async def server_info_send(command, send_title):
    result = subprocess.check_output(command,shell=True)
    send_data = result.decode().strip().split('\n')
    channel = client.get_channel(int(CHANNEL_SERVER_ID))
    await channel.send(send_title)
    for i in range(len(send_data)):
        await channel.send(send_data[i])

@client.event
async def on_ready():
    print('Logged in done.')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/test':
        await message.channel.send('test message')
    if message.content == '/df':
        await server_info_send("df -h | grep /dev/vda3", "[Server Info] ストレージ情報")
    if message.content == '/free':
        await server_info_send("free -m", "[Server Info] メモリ情報")

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