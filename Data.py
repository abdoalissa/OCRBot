from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can extract text from images using OCR technology.

By @abdoalissa
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨ مطور من قبل عبداللطيف العيسى ,  facebook :  ✨", url="https://www.facebook.com/abdo.alissa.me")],
        [InlineKeyboardButton(text="🏠 العودة للصفحة الرئيسية 🏠", callback_data="الرئيسية")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ مطور من قبل عبداللطيف العيسى ,  Facebook : ✨", url="https://www.facebook.com/abdo.alissa.me")
        ],
        [
            InlineKeyboardButton("كيف يمكن استخدامه ؟ ❔", callback_data="مساعدة"),
            InlineKeyboardButton("🎪 حول البوت 🎪", callback_data="حول")
        ],
        [InlineKeyboardButton("♥ التواصل مع المطور  ♥", url="https://t.me/abdoalissa")],
        [InlineKeyboardButton("🎨 الدعم  🎨", url="https://t.me/abdoalissa")],
    ]

    # Help Message
    HELP = """
You Really Need Help ?!?!?!?!

Just send an image. Rest is on me.

Note : You can send any amount of images at once and it will work with same speed and accuracy.

More features in development. Keep track by contact @abdoalissa .
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @abdoalissa

Source Code : contact with me please :) :) 

Framework : just python

Language : [Python](www.python.org)

Developer : @abdoalissa
    """
