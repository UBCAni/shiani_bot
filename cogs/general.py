from discord.ext import commands
from random import choice

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def choose(self, ctx, *args):
        if (len(args) < 2):
            await ctx.send("Not enough options to pick from.")
        else:
            await ctx.send(f'{choice(args)}')


async def setup(bot):
    await bot.add_cog(General(bot))
