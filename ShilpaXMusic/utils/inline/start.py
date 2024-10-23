from pyrogram.types import InlineKeyboardButton

import config
from ShilpaXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [ InlineKeyboardButton(text="๛ᴍʀ.sᴏᴍᴜ࿐", url=f"https://t.me/alone_somu6")],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_6"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_5"], url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [ InlineKeyboardButton(text="๛ᴍʀsᴏᴍᴜ࿐", url=f"https://t.me/alone_somu6")],
    ]
    return buttons