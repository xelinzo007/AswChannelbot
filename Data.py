from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}
Welcome to {}
You can use me to manage channels with tons of features. Use below buttons to learn more !
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="Home", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✖️enon ● Updates", url="https://t.me/xmusicbots")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("About ", callback_data="about")
        ],
        [InlineKeyboardButton("✖️enon ● Network", url="https://t.me/Xenonbots")],
        [InlineKeyboardButton("Support Group", url="https://t.me/Xenonsupportchat")],
    ]

    # Help Message
    HELP = """
Everything is self explanatory after you add a channel.
To add a channel use keyboard button 'Add Channels' or alternatively for ease, use `/add` command

**Available Commands**

/about - About The Bot
/help - This Message
/start - Start the Bot

Alternative Commands
/channels - List added Channels
/add - Add a channel
/report - Report a Problem
    """

    # About Message
    ABOUT = """
**About This Bot** 
channel auto posting bot
from @xenonbots
    """
