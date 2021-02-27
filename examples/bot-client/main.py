import os
import discord
from discord.ext import commands, levenshtein


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print('Bot is ready')
        levenshtein.Levenshtein(self, max_length=3)

    async def on_command_suggest(self, ctx, suggested_commands):
        body = 'suggested commands: ' + ' '.join([f'`{command}`' for command in suggested_commands])
        await ctx.send(body)


bot = MyBot(command_prefix='+', intents=discord.Intents.all())


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.group(invoke_without_command=True)
async def math(ctx):
    await ctx.send('this is a math cog')


@math.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

bot.run(os.environ['BOT_TOKEN'])
