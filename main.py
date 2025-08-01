# main.py

import os
from dotenv import load_dotenv
from selfbot import SelfBot
from tldr import setup_tldr

load_dotenv()

bot = SelfBot(
    token="MTEwNTUwMTkxMjYxMjIyOTE0MQ.GwtYQv.oDGpOK6_LTPwUXVml3HesREkZcTwlg_Zz9GLu8",
    prefix="!",
)

setup_tldr(bot)

if __name__ == "__main__":
    bot.run()
