discord-ext-levenshtein
#######################

A discord.py extension for command name suggestion

|Docs| |PyPI| |Support| |Lint| |Build|

Installation
============

.. code-block:: sh

    # Windows
    py -3 -m pip install --upgrade discord-ext-levenshtein

    # Linux
    python3 -m pip install --upgrade discord-ext-levenshtein

Usage
=====

The extension will be enabled by creating ``levenshtein.Levenshtein``
when ``on_ready`` is called.

.. code-block:: python

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

For more usage, refer to `the examples directory <https://github.com/shirataki2/discord-ext-levenshtein/tree/master/examples>`_

.. |Docs| image:: https://readthedocs.org/projects/discord-ext-levenshtein/badge/?version=latest
    :target: https://discord-ext-levenshtein.readthedocs.io/en/latest/?badge=latest

.. |Build| image:: https://github.com/Shirataki2/discord-ext-levenshtein/actions/workflows/build.yml/badge.svg
    :target: https://github.com/Shirataki2/discord-ext-levenshtein/actions/workflows/build.yml

.. |Lint| image:: https://github.com/Shirataki2/discord-ext-levenshtein/actions/workflows/linting.yml/badge.svg
    :target: https://github.com/Shirataki2/discord-ext-levenshtein/actions/workflows/linting.yml

.. |PyPI| image:: https://badge.fury.io/py/discord-ext-levenshtein.svg
    :target: https://pypi.org/project/discord-ext-levenshtein/

.. |Support| image:: https://img.shields.io/pypi/pyversions/discord-ext-levenshtein.svg
    :target: https://pypi.org/project/discord-ext-levenshtein/
