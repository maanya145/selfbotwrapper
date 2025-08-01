# selfbot.py

import os
import discord
from discord.ext import commands

class SelfBot:
    def __init__(self, *, token: str = None, prefix: str = "?"):
        """
        A simple wrapper around discord.py-self for creating selfbots.

        Args:
            token: Your Discord user token. If not provided, will try DISCORD_TOKEN env var.
            prefix: The command prefix to listen for.
        """
        self.token = token or os.getenv("DISCORD_TOKEN")
        if not self.token:
            raise ValueError("Discord token must be provided either as argument or DISCORD_TOKEN env var.")

        # instantiate the Bot with `self_bot=True`
        self.bot = commands.Bot(
            command_prefix=prefix,
            self_bot=True,
         #   help_command=None,       # disable default help if you want your own
            #intents=discord.Intents.default()
        )

        # expose direct access if needed
        self.prefix = prefix

        # hook default events
        @self.bot.event
        async def on_ready():
            print(f"[SELF-BOT] Logged in as {self.bot.user} (ID: {self.bot.user.id})")

        @self.bot.event
        async def on_message(message: discord.Message):
            # ignore messages not sent by us
            if message.author.id != self.bot.user.id:
                return

            # process commands if they start with prefix
            if message.content.startswith(self.prefix):
                # let commands.Bot handle it
                await self.bot.process_commands(message)

    def command(self, name: str = None, **kwargs):
        """
        Decorator to register a command on the selfbot.

        Usage:
            @bot.command("foo")
            async def _(ctx, ...):
                ...

        If name is None, decorator will use the function name.
        """
        return self.bot.command(name=name, **kwargs)

    def event(self, coro):
        """
        Shortcut decorator to register arbitrary events.
        """
        return self.bot.event(coro)

    def run(self):
        """
        Start the bot. Blocks until shutdown.
        """
        self.bot.run(self.token, bot=False)
