import os 

import random

from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 

from pyrogram.errors import UserNotParticipant, UserBannedInChannel

HB = Client(

    "MSG_DELETING Bot",

    bot_token = os.environ["BOT_TOKEN"],

    api_id = int(os.environ["API_ID"]),

    api_hash = os.environ["API_HASH"]

)  

START_TEXT = """**HI {}, 

I CAN GENERATE RANDOM PET NAMES FOR YOU 

JUST PRESS HELP BUTTON

TO KNOW HOW TO USE ME

MADE BY @TELSABOTS**

"""

HELP_TEXT = """

JUST SENT /NAME 

THEN I WILL SENT PET NAMES 

100 PET NAMES AVAILABLE 

MADE BY @TELSABOTS

"""

ABOUT_TEXT = """

 🤖<b>BOT:PET NAME 🤖</b>

 

📢<b>CHANNEL :</b> @TELSA BOTS

🧑🏼‍💻DEV🧑🏼‍💻: @ALLUADDICT

"""

START_BUTTONS = InlineKeyboardMarkup(

        [[

        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),

        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')

        ],[

        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),

        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),

        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')

        ]]

    )

HELP_BUTTONS = InlineKeyboardMarkup(

        [[

        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),

        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')

        ],[

        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),

        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),

        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')

        ]]

    )

ABOUT_BUTTONS = InlineKeyboardMarkup(

        [[

        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),

        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')

        ],[

        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),

        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),

        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')

        ]]

    )

@HB.on_callback_query()

async def cb_data(bot, update):

    if update.data == "home":

        await update.message.edit_text(

            text=START_TEXT.format(update.from_user.mention),

            disable_web_page_preview=True,

            reply_markup=START_BUTTONS

        )

    elif update.data == "help":

        await update.message.edit_text(

            text=HELP_TEXT,

            disable_web_page_preview=True,

            reply_markup=HELP_BUTTONS

        )

    elif update.data == "about":

        await update.message.edit_text(

            text=ABOUT_TEXT,

            disable_web_page_preview=True,

            reply_markup=ABOUT_BUTTONS

        )

    else:

        await update.message.delete()

    

@HB.on_message(filters.command(["start"]))

async def start(bot, update):

    text = START_TEXT.format(update.from_user.mention)

    reply_markup = START_BUTTONS

    await update.reply_text(

        text=text,

        disable_web_page_preview=True,

        reply_markup=reply_markup

    )

    

@HB.on_message(filters.command(["help"]))

async def help_message(bot, update):

    text = HELP_TEXT

    reply_markup = HELP_BUTTONS

    await update.reply_text(

        text=text,

        disable_web_page_preview=True,

        reply_markup=reply_markup

    )     

    

@HB.on_message(filters.command(["about"]))

async def about_message(bot, update):

    text = ABOUT_TEXT

    reply_markup = ABOUT_BUTTONS

    await update.reply_text(

        text=text,

        disable_web_page_preview=True,

        reply_markup=reply_markup

    )     

    

NAMES = ["","**BELLA\nJOIN @TELSABOTS**","**CLEO\nJOIN @TELSABOTS**","**ROBIN\nJOIN @TELSABOTS**","**WOOD STOCK\nJOIN @TELSABOTS**","**BUDDY\nJOIN @TELSABOTS**",

"**BUFFON\nJOIN @TELSABOTS**","**PLUCKY\nJOIN @TELSABOTS**","**ZEZO\nJOIN @TELSABOTS**","**ZAZU\nJOIN @TELSABOTS**","**SCRUFFY\nJOIN @TELSABOTS**", "**BRUNO\nJOIN @TELSABOTS**",

"**BABY\nJOIN @TELSABOTS**","**PEPPER\nJOIN @TELSABOTS**","**GEORGE\nJOIN @TELSABOTS**","**RITA\nJOIN @TELSABOTS**","**ARTHUR\nJOIN @TELSABOTS**","**JEWEL\nJOIN @TELSABOTS**","**TUCK\nJOIN @TELSABOTS**",

"**ANDROMEDA\nJOIN @TELSABOTS**","**FANG\nJOIN @TELSABOTS**","**GOYLE\nJOIN @TELSABOTS**","**GODRIC\nJOIN @TELSABOTS**","**GRAWP\nJOIN @TELSABOTS**","**GOYLE\nJOIN @TELSABOTS**","**HEDWIG\nJOIN @TELSABOTS**","**LUCKY\nJOIN @TELSABOTS**","**CORMAC\nJOIN @TELSABOTS**",

"**HAGRID\nJOIN @TELSABOTS**","**FLEUR\nJOIN @TELSABOTS**","**BLAISE\nJOIN @TELSABOTS**","**BLIZZ\nJOIN @TELSABOTS**","**BILL\nJOIN @TELSABOTS**","**DRACO\nJOIN @TELSABOTS**",

"**DUDLEY\nJOIN @TELSABOTS**","**FAWKES\nJOIN @TELSABOTS**","**BATHILDA\nJOIN @TELSABOTS**","**ARGUS\nJOIN @TELSABOTS**","**QUEEN\nJOIN @TELSABOTS**","**TOMMY\nJOIN @TELSABOTS**","**TIMMY\nJOIN @TELSABOTS**",

"**BEAN\nJOIN @TELSABOTS**","**CUB\nJOIN @TELSABOTS**","**ZUZU\nJOIN @TELSABOTS**","**PIGLET\nJOIN @TELSABOTS**","**ROCKY\nJOIN @TELSABOTS**","**JASPER\nJOIN @TELSABOTS**",

"**SCOOBY\nJOIN @TELSABOTS**","ZEUS\nJOIN @TELSABOTS**""**SILKY\nJOIN @TELSABOTS**\nJOIN @TELSABOTS**","**PEARL\nJOIN @TELSABOTS**","**RUBY\nJOIN @TELSABOTS**","**ERROL\nJOIN @TELSABOTS**",

"**LOIS\n JOIN @TELSABOTS**","**CLIFFORD\nJOIN @TELSABOTS**","**TOBIN\nJOIN @TELSABOTS**","**STELLA\nJOIN @TELSABOTS**","**LOGAN\nJOIN @TELSABOTS**","**MURPHY\nJOIN @TELSABOTS**",

"**OSCAR\nJOIN @TELSABOTS**","**PIPER\nJOIN @TELSABOTS**","**RANGER\nJOIN @TELSABOTS**","**KITTY\nJOIN @TELSABOTS**","**LZZY\nJOIN @TELSABOTS**","**PICASSO\nJOIN @TELSABOTS**",

"**CHARLIE\nJOIN @TELSABOTS**","**LASSIE\nJOIN @TELSABOTS**","**BENJI\nJOIN @TELSABOTS**","**KING\nJOIN @TELSABOTS**","**SCOUT\nJOIN @TELSABOTS**T","**SMUDGE\nJOIN @TELSABOTS**",

"**OPAL\nJOIN @TELSABOTS**","**JIMMY\nJOIN @TELSABOTS**","**BAILEY\nJOIN @TELSABOTS**","**SASHA\nJOIN @TELSABOTS**","**BENJI\nJOIN @TELSABOTS**","**CLOONEY\nJOIN @TELSABOTS**",

"**PERRY\nJOIN @TELSABOTS**","**SIMBA\nJOIN @TELSABOTS**","**ANGEL\nJOIN @TELSABOTS**","**OREO\nJOIN @TELSABOTS**","**BUTTERS\nJOIN @TELSABOTS**","**ZOLA\nJOIN @TELSABOTS**",

"**PUMPKIN\nJOIN @TELSABOTS**","**LUNA\nJOIN @TELSABOTS**","ZOE","**LOLA\nJOIN @TELSABOTS**","OLIVER","**LOKI\nJOIN @TELSABOTS**","**MAX\nJOIN @TELSABOTS**","**OLLIE\nJOIN @TELSABOTS**",

    ]

result_BUTTONS = InlineKeyboardMarkup(

        [[

        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),

        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')

        ]]

    )

reply_markup=result_BUTTONS

@HB.on_message(filters.command(["name", "name"]))

async def NAME(client, message):

    petname = random.choice(NAMES)

    if message.reply_to_message:

        await message.reply_to_message.reply_text(petname,reply_markup=reply_markup)

    else:

        await message.reply_text(petname ,reply_markup=reply_markup)

    

HB.run()

print("hb")
