import os
import discord
from dotenv import load_dotenv
# import sys

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


bot = discord.Client()

@bot.event
async def on_ready():
    for guild in bot.guilds:
      guild_count = 0
      print(f"(id: {guild.id}) (name: {guild.name})")
      guild_count = guild_count + 1
    print("DiscordBot is in " + str(guild_count) + " guilds.")
@bot.event
async def on_message(message):
    #print(f"checking")
    if bot.user.mentioned_in(message):
        await message.channel.send('You mentioned me!')


bot.run(TOKEN)

