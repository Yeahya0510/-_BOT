import discord
from discord.ext import commands
import json
import random, os, asyncio


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='[', intents = intents)

@bot.event
async def on_ready():
   print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(827844482983657482)
    await channel.send(f'{member} join!')
    
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(827844482983657482)
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')



bot.run('ODI3NTkzNTIzMjQyNzI5NDky.YGdShw.RwDaLuoBC1ZHeab983FLeSYYgXI')