import os 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from pyrogram.errors import UserNotParticipant, UserBannedInChannel


HB = Client(
    "Echo-bot", 
    api_id = 2152187,
    api_hash = "1a0208e94456f4799a5f5269f1198d62",
    bot_token = "5510758631:AAG2mbmf7-kKseNsbPBGRGvRaSu2md4c6FQ"
    
)     
Username = "THOR_online"



START_TEXT = """HI {}, 
I CAN PROVIDE MOVIES 
MADE BY @TELSABOTS
"""
HELP_TEXT = """
JIUST SENT ANY MOVIE NAME 
❌DONT SENT YEAR 
❌ DONT SENT LANGAUGES 
✅ONLY SENT MOVIE NAME 
eg:- KGF2 

MADE BY @TELSABOTS
"""
ABOUT_TEXT = """
 🤖<b>BOT:DISCUSS UNPIN🤖</b>
 
📢<b>CHANNEL :</b> ❤️ <a href='https://t.me/telsabots'>TELSA BOTS❤️</a>

🧑🏼‍💻DEV🧑🏼‍💻: @ALLUADDICT

 
🤩<b>SOURCE :</b> 🤩 <a href='https://hbamal.blogspot.com/2021/08/how-to-make-your-own-discussion-unpin_4.html'>CLICK HERE❤️</a>

"""
feedback_text ="""**😍DUDE YOU CAN REQUEST \n MOVIE THROUGH HERE \n\n😉JUST SENT MOVIE NAME\n\neg:-/feedback kgf2**"""
SOURCE_TEXT = """</b>PRESS SOURCE BUTTON FOR SOURCE 
AND WATCH TOTOURIAL VIDEO IF YOU WANT ANY HELP</b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩SOURCE🤩', url='https://hbamal.blogspot.com/2021/08/how-to-make-your-own-discussion-unpin_4.html'),
        InlineKeyboardButton('💟TOTOURIAL💟', url='https://www.youtube.com/watch?v=sXTg5CB9dy8')
        ],[
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
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
        InlineKeyboardButton('🤩SOURCE🤩', url='https://youtu.be/sXTg5CB9dy8')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
FEEDBACK_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡FEEDBACK🏡', callback_data='feedback'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
close_buttons = InlineKeyboardMarkup(
        [[
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
    elif update.data == "feedback":
        await update.message.edit_text(
            text=feedback_text,
            disable_web_page_preview=True,
            reply_markup =close_buttons
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


@HB.on_message(filters.command(["feedback"]))
async def my_handler(client, message):
    await message.forward(Username)

 
jana="""🎬 Title : Jana Gana Mana\n🗓 Year : 2022\n🔊 Language : #Malayalam\n💿 Quality : HDRip\n📂 Uploaded :@FILM_CUBE_TM"""

jana_buttons = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('🤩DOWNLOAD 🤩', url='https://t.me/+FR6KtHW8llNjYWM1')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
    ]]
    
)

@HB.on_message(filters.text & filters.private & ~filters.group)
async def files(Bot, message): 
    if message.text.lower() == 'jg':
        await message.reply_photo( photo="https://telegra.ph/file/b61e7e25d5f78d2fbe984.jpg", caption=jana, reply_markup=jana_buttons)
    else:
        await message.reply_text("**😕SORRY BRO\nNOTHING FOUND\n\n👇PRESS FEEDBACK BUTTON \n😇TO REQUEST MOVIES", reply_markup=FEEDBACK_BUTTONS)



print("HB")
HB.run()




