import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
#TOKEN = "OTM1NTc0NDY3Mzk1MDY3OTM1.YfAnnw.6Tt7CUpdNxfPemPyZiVuC1nkE44"

bot = discord.Client()

@bot.event
async def on_ready():
    for guild in bot.guilds:
      guild_count = 0
      print(f"- {guild.id} (name: {guild.name})")
      guild_count = guild_count + 1
    print("DiscordBot is in " + str(guild_count) + " guilds.")


bot.run(TOKEN)
