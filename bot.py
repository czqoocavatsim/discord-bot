import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print ("Starting up")
    activity = discord.Activity(name="the HF radios", type=discord.ActivityType.listening)
    await bot.change_presence(activity=activity)

@bot.command()
async def ping(ctx):
    await ctx.send(":ping_pong: Ping, pong! {0}ms".format(round(bot.latency, 1)))


bot.run(TOKEN)