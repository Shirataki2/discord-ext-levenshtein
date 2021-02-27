from discord.ext import commands
from Levenshtein import distance
from typing import List


class InnerLevenshtein(commands.Cog):
    def __init__(self, bot: commands.Bot, max_length: int, command_names: List[str]):
        self.bot = bot
        self.max_length = max_length
        self.command_names = command_names

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        if isinstance(exception, commands.CommandNotFound):
            body: str = ctx.message.content
            body = body.lstrip(ctx.prefix)
            self.bot.dispatch('command_suggest', ctx, self.suggest_command(body))

    def suggest_command(self, command_name: str) -> List[str]:
        suggested_commands = []
        for command in self.command_names:
            dist = distance(command, command_name)
            if dist <= self.max_length:
                suggested_commands.append((dist, command))

        return [command[1] for command in sorted(suggested_commands)]
