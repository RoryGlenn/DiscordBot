import discord
import asyncio

from threading import Thread
from discord.ext import commands, tasks

CHANNEL_ID = 0 # ENTER CHANNEL ID AS INT
TOKEN      = "ENTER TOKEN HERE"

client   = commands.Bot(command_prefix='.')
g_status = "DEFAULT"


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Online"))


@client.command()
async def status(ctx):
    global g_status
    await ctx.send(g_status)


@tasks.loop(seconds=5, count=None)
async def update_loop(string):
    await client.wait_until_ready()
    await client.change_presence(status=discord.Status.online, activity=discord.Game(string))


@tasks.loop(seconds=1, count=1)
async def update_status(string):
    await client.wait_until_ready()
    await client.change_presence(status=discord.Status.online, activity=discord.Game(string))


def discord_bot_init():
    loop = asyncio.get_event_loop()
    loop.create_task(client.start(TOKEN))
    Thread(target=loop.run_forever).start()


discord_bot_init()