# bot.py
import os
from discord.ext import commands
from dotenv import load_dotenv
import Greetings
import Random

print(f'Connecting...')

# Load Environment Variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_NAME = os.getenv('DISCORD_GUILD')

# Sets the command prefix to be a / in Discord
bot = commands.Bot(command_prefix='/')

# Set up all the cogs needed for the bot to run
# https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
#
bot.add_cog(Greetings.Greetings(bot))
bot.add_cog(Random.Random(bot))


@bot.event
async def on_message(message):
    content = message.content.lower()
    print(message)
    print(message.author)

    if message.author == bot.user:
        return

    if 'party' in content:
        author = str(message.author.nick)
        await message.channel.send(f"Fuck yeah {author}, let's get the party started!")

    if os.getenv('T_HIDDEN') in content:
        await message.channel.send(os.getenv('T_RESPONSE'))


# Start the Bot
print(f'Connected to the Discord Server - {GUILD_NAME}')
bot.run(TOKEN)

