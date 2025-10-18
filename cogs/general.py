from encodings.aliases import aliases

from discord.ext import commands
from random import choice
import random

MAX_ROLL = 2 ** 63 - 1


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["8ball", "ball"])
    async def _8ball(self, ctx, *, question):
        """Ask 8 ball a question.

                Question must end with a question mark.
        """
        ball = [
            "As I see it, yes",
            "It is certain",
            "It is decidedly so",
            "Most likely",
            "Outlook good",
            "Signs point to yes",
            "Without a doubt",
            "Yes",
            "Yes – definitely",
            "You may rely on it",
            "Reply hazy, try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful",
        ]

        if question.endswith("?") and question != "?":
            await ctx.send(choice(ball))
        else:
            await ctx.send("That doesn't look like a question.")

    @commands.command()
    async def choose(self, ctx, *choices):
        """Choose between multiple options.

        There must be at least 2 options to pick from.
        Options are separated by spaces.

        To denote options which include whitespace, you should enclose the options in double quotes.
        """
        if (len(choices) < 2):
            await ctx.send("Not enough options to pick from.")
        else:
            await ctx.send(f'{choice(choices)}')

    @commands.command()
    async def flip(self, ctx):
        """Flip a coin."""
        await ctx.send(f'*Flips a coin and... {choice(["HEADS", "TAILS"])} !*')

    @commands.command()
    async def roll(self, ctx, number=100):
        """Roll a random number.

               The result will be between 1 and `<number>`.

               `<number>` defaults to 100.
        """
        if (number <= 1):
            await ctx.send("Please choose a number higher than 1")
        elif (number >= MAX_ROLL):
            await ctx.send("Please choose a smaller number!")
        else:
            val = random.randint(1, number)
            await ctx.send(f'The rolled number is: {val}')


async def setup(bot):
    await bot.add_cog(General(bot))
