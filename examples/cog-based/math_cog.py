from discord.ext import commands
import math


class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['a'])
    async def add(self, ctx, a: int, b: int):
        await ctx.send(a + b)

    @commands.command(aliases=['m','multiply'])
    async def mul(self, ctx, a: int, b: int):
        await ctx.send(a * b)

    @commands.group(aliases=['constants'], invoke_without_command=True)
    async def consts(self, ctx):
        await ctx.send_help('consts')

    @consts.command()
    async def pi(self, ctx):
        await ctx.send(f'{math.pi}')

    @consts.command(aliases=['2pi'])
    async def tau(self, ctx):
        await ctx.send(f'{math.pi*2.0}')

    @consts.command()
    async def e(self, ctx):
        await ctx.send(f'{math.e}')


def setup(bot):
    bot.add_cog(Math(bot))
