#Project_By mnwuPark KongBot.py
import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get_slots
from discord import FFmpegPCMAudio

token = ""

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = ".", intents = intents)

@bot.event
async def on_ready():
    print("Login to:", bot.user.name)
    print("Bot id:", bot.user.id)
    print("Bot Connection has succesful !")
    await bot.change_presence(status = discord.status.online, activity = discord.Game("Upload, Patch.."))

@bot.command
async def join(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
        await ctx.send(embed = discord.Embed(title = "Kong", description = "Joined your channel..", color = 0x000000))
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send(embed = discord.Embed(title = "Kong", description = "You didn't joined any channel :(", color = 0x000000))

@bot.command
async def leave(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send(embed = discord.Embed(title = "Kong", description = "I didn't joined any channel :(", color = 0x000000))

@bot.command
async def say(ctx, *, text):
    await ctx.send(embed = discord.Embed(title = "Say", description = text, color = 0xffffff))

@bot.command
async def play(ctx, *, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download = False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.sned(embed = discord.Embed(title = "Play Music", description = "Play Music:" + url, color = 0xffffff))
    else:
        await ctx.send("Music has been played now !")

bot.run(token)