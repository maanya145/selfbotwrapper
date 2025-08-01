from selfbot import SelfBot

bot = SelfBot(
    token="YOUR_DISCORD_TOKEN",
    prefix="?",
)

@bot.command("echo")
async def _(ctx, *, rest: str):
    """Echo back whatever was passed."""
    await ctx.reply(rest, mention_author=False)

# register any other commands/handlers...

if __name__ == "__main__":
    bot.run()
