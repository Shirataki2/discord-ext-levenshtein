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
bot.load_extension('math_cog')

bot.run(os.environ['BOT_TOKEN'])
