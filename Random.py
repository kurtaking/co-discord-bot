from discord.ext import commands
import random
import requests
import os


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def coinflip(self, ctx):
        coin = 'Heads'
        odds = random.randint(0, 3)

        if odds == 1:
            coin = 'Tails'

        await ctx.send(coin)

    @commands.command()
    async def dice(self, ctx, number_of_dice: int, number_of_sides: int):
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]

        await ctx.send(', '.join(dice))

    @commands.command()
    async def joke(self, ctx):
        headers = {
            'Accept': 'application/json'
        }

        response = requests.get(os.getenv('JOKE_API_URL'), headers=headers)
        joke = response.json()['joke']

        await ctx.send(joke)

    @commands.command()
    async def insult(self, ctx, *, member):
        insult_member = member

        if 'myself' in member or 'me' in member:
            insult_member = ctx.author.name
            insult_member = str(insult_member)

        headers = {
            'Accept': 'application/json'
        }

        response = requests.get(os.getenv('INSULT_API_URL'), headers=headers)
        insult = response.json()['insult']

        await ctx.send(insult_member + ', ' + insult)
