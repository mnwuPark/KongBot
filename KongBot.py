#Project_By mnwuPark KongBot.py
import discord
from discord.ext import commands

token = ""

bot = commands.Bot(command_prefix = ".")

@bot.event
async def on_ready():
    print("Login to:", bot.user.name)
    print("Bot id:", bot.user.id)
    print("Bot Connection has succesful !")
    await bot.change_presence(status = discord.status.online, activity = None)

bot.run(token)