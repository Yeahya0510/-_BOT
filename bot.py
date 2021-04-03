import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix= '[', intents = intents)

@bot.event
async def on_ready():
    print("> > Watson is Online~ < <")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(827844482983657482)
    await channel.send(f'{member} 進來了可晴的小學,一起歡迎他/她吧~')
    
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(827844482983657482)
    await channel.send(f'{member} 從可晴的小學畢業了')


bot.run('ODI3NTkzNTIzMjQyNzI5NDky.YGdShw.YF2zNKpIUxR6MlzyhdX-M-ABrLY')