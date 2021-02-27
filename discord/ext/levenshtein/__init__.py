from collections import namedtuple
from discord.ext import commands
from typing import List

from .cogs.levenshtein import InnerLevenshtein

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')
version_info = VersionInfo(major=0, minor=2, micro=1, releaselevel='alpha', serial=0)

__version__ = '.'.join(map(str, [version_info.major, version_info.minor, version_info.micro]))


class Levenshtein:
    """The root of the module.

    Creates a list of commands when ``on_ready`` is called,
    and dispatches the ``on_command_suggest`` coroutine
    when command_not_found is invoked.

    Args:
        bot (:class:`~discord.ext.commands.Bot`):
            discord.py bot instance
        max_length (int):
            The Levenshtein distance threshold
            for considering a similar command.

            the Levenshtein distance is a string metric
            for measuring the difference between
            two sequences.
            
            Informally, the Levenshtein distance
            between two words is the minimum number
            of single-character edits
            (insertions, deletions or substitutions)
            required to change one word into the other.

    Note:
        When CommandNotFound exception is raised
        in discord.py, ``command_suggest`` event will be dispatched.

        The ``command_suggest`` event is given two arguments,
        the former is the Context(:obj:`~discord.ext.commands.Context`) and
        the latter is a list of similar commands
        (``List(str)``).

    """

    def __init__(self, bot: commands.Bot, max_length=3):
        self.bot = bot
        self._command_names: List[str] = []
        self._listup_commands(self.bot)
        self.max_length = max_length
        cog = InnerLevenshtein(self.bot, self.max_length, self._command_names)
        self.bot.add_cog(cog)

    def _listup_commands(self, group, prefix=None):
        if prefix is None:
            prefix = []

        prefix_str = ' '.join(prefix) + ' ' if len(prefix) > 0 else ''

        for command in group.commands:
            if command.hidden:
                continue

            elif isinstance(command, commands.Group):
                self._command_names.append(prefix_str + command.name)
                prefix.append(command.name)
                self._listup_commands(command, prefix)
                prefix.pop()

            elif isinstance(command, commands.Command):
                self._command_names.append(prefix_str + command.name)
