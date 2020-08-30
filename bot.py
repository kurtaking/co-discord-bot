# bot.py
import os

from discord.ext import commands
from dotenv import load_dotenv

import Greetings
import Random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
bot.add_cog(Greetings.Greetings(bot))
bot.add_cog(Random.Random(bot))


bot.run(TOKEN)
