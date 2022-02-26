import asyncio
import os
import re
import sys

import telethon.utils
from telethon import Button, TelegramClient, custom, events

from userbot.Config import Config
from userbot.start import abuses, addons, assistants, hekp, install, module, spams

from . import LOGS, LEGENDversion, bot

l1 = Config.HANDLER
l2 = Config.SUDO_HANDLER
LEGEND_PIC = "https://telegra.ph/file/e753315316673cff51085.mp4"

perf = "[ Pro Lêɠêɳ̃dẞot ]"

onbot = "start - Check if I am Alive \nping - Pong! \ntr - <lang-code> \nbroadcast - Sends Message To all Users In Bot \nid - Shows ID of User And Media. \naddnote - Add Note \nnotes - Shows Notes \nspam - spam value text (value < 100)\nbigspam - spam value text (value > 100) \nraid - Raid value Reply to Anyone \nreplyraid - Reply To Anyone \ndreplyraid - Reply To Anyone \nrmnote - Remove Note \nalive - Am I Alive? \nbun - Works In Group , Bans A User. \nunbun - Unbans A User in Group \nprumote - Promotes A User \ndemute - Demotes A User \npin - Pins A Message \nstats - Shows Total Users In Bot \npurge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \ndel - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"

bot_father = "@BotFather"

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"


async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"PRO_STRING - {str(e)}")
        sys.exit()


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("♥️ Starting PRO-LEGENDBOT ♥️")
            bot.loop.run_until_complete(add_bot(Config.BOT_USERNAME))
            LOGS.info("🥇🔥 PRO-LEGENDBOT Startup Completed 🔥🥇")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

print("📍⚜Loading Modules / Plugins⚜✔")

tgbot = bot.tgbot


async def killer():
    LEGEND_USER = bot.me.first_name
    Pro_LegendBoy = bot.uid
    legd_mention = f"[{LEGEND_USER}](tg://user?id={Pro_LegendBoy})"
    name = f"{legd_mention}'s Assistant"
    description = (
        f"I am Assistant Of {legd_mention}.This Bot Can Help U To Chat With My Master"
    )
    starkbot = await tgbot.get_me()
    bot_id = starkbot.first_name
    if bot_id.endswith("t"):
        print("Bot Starting")
    else:
        try:
            await bot.send_message("@BotFather", "/setinline")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", perf)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setcommands")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", onbot)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setname")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", name)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", description)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setuserpic")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_file("@BotFather", "userbot/resources/pics/main.jpg")
            await asyncio.sleep(2)
        except Exception as e:
            print(e)
    # else:
    # print("Turn On ASSISTANT to Use This")


async def legends():
    LEGEND_USER = bot.me.first_name
    Pro_LegendBoy = bot.uid
    legd_mention = f"[{LEGEND_USER}](tg://user?id={Pro_LegendBoy})"
    yescaption = f"Hello Sir/Miss Something Happened \nDing Dong Ting Tong Ping Pong\nSuccessfully PRO-LEGENDBOT Has Been Deployed \nMy Master ~ 『{legd_mention}』 \nVersion ~ {LEGENDversion}\nClick Below To Know More About Me👇🏾👇👇🏼"
    try:
        TRY = [[Button.inline("⭐ Start ⭐", data="start")]]
        await tgbot.send_file(
            bot.me.id, LEGEND_PIC, caption=yescaption, buttons=TRY, incoming=True
        )
    except:
        pass


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"start")))
async def help(event):
    starkbot = await tgbot.get_me()
    bot_id = starkbot.first_name
    if event.query.user_id is not bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message=f"Hey Sir It's Me {bot_id}, Your Assistant! How Can I Help U?",
            buttons=[
                [
                    Button.url(" Support ", "https://t.me/LegendBot_Pros"),
                    Button.url(" Updates ", "https://t.me/Pro_LegendBots"),
                ],
                [
                    custom.Button.inline("Users", data="users"),
                    custom.Button.inline("Settings", data="osg"),
                ],
                [custom.Button.inline("Hack", data="hack")],
            ],
        )
    else:
        await event.answer("Sorry U Cant Acces This Button", cache_time=0, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"restart")))
async def restart(event):
    if event.query.user_id == bot.uid:
        await event.answer("Restarting Please Wait 4 min... ", cache_time=0, alert=True)
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
    else:
        await event.answer(
            "Sorry Only My Master Can Access It", cache_time=0, alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"osg")))
async def help(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message="Which Type Of Setting Do U Want Sir",
            buttons=[
                [
                    custom.Button.inline("Restart", data="restart"),
                    custom.Button.inline("Reload", data="reload"),
                ],
                [
                    custom.Button.inline("Var", data="strvar"),
                    custom.Button.inline("Commmands", data="gibcmd"),
                ],
                [custom.Button.inline("Back", data="start")],
            ],
        )
    else:
        await event.answer(
            "Sorry Only My Master Can Access This Button", cache_time=0, alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"reload")))
async def rel(event):
    if event.query.user_id == bot.uid:
        await event.answer(
            "Reloading Lêɠêɳ̃dẞø†... Wait for few seconds...", cache_time=0, alert=True
        )
        await reload_LEGENDBOT()
    else:
        await event.answer(
            "Sorry U Dont Have Access to Use this Button", cache_time=0, alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"strvar")))
async def help(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message="Which Type Of Setting Do U Want Sir",
            buttons=[
                [
                    custom.Button.inline("Var Explain", data="var"),
                    custom.Button.inline("All Var", data="allvar"),
                ],
                [custom.Button.inline("Back", data="osg")],
            ],
        )
    else:
        await event.answer("Sorry This Button Only My Master", cache_time=0, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"var")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message=".set var <varname> <value> ex:- .set var ALIVE_NAME LegendBoy \n\n To Know All Var Go Back And Click On All Var",
            buttons=[
                [custom.Button.inline("Back", data="osg")],
            ],
        )
    else:
        await event.answer("Sorry This Button Only My Master", cache_time=0, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"allvar")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message="All Var Name Are Given Below :\n\nABUSE = ON/ OFF\nALIVE_EMOJI = ANY EMOJI, Example: ✨\nALIVE_MESSAGE = Any Message ,Example : PRO-LEGENDBOT Is Online\nALIVE_PIC = telegraph Link, use .tm to get it\nASSISTANT = ON / OFF\nAWAKE_PIC = telegraph link, get from .tm<reply to pic>\n",
            buttons=[
                [custom.Button.inline("Back", data="osg")],
            ],
        )
    else:
        await event.answer("Sorry This Button Only My Master", cache_time=0, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def users(event):
    if event.query.user_id == bot.uid:
        grabon = "Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot \n➤ /purge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \n➤ /del - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"
        await tgbot.send_message(event.chat_id, grabon)
    else:
        await event.answer(
            "Wait A Min, U Are Not My Master So How Dare U Trying To Touch This Button",
            cache_time=0,
            alert=True,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
async def help(event):
    await event.delete()


menu = """
Reply To My Message If I am using In Group
"A" :~ [Check user own groups and channels]

"B" :~ [Check user all information like phone number, usrname... etc]

"C" :~ [Ban a group {give me StringSession and channel/group username i will ban all members there}]

"D" :~ [Know user last otp {1st use option B take phone number and login there Account then use me i will give you otp}]

"E" :~ [Join A Group/Channel via StringSession]

"F" :~ [Leave A Group/Channel via StringSession]

"G" :~ [Delete A Group/Channel]

"H" :~ [Check user two step is eneable or disable]

"I" :~ [Terminate All current active sessions except Your StringSession]

"J" :~ [Delete Account]

"K" :~ [Demote all admins in a group/channel]

"L" ~ [Promote a member in a group/channel]

"M" ~ [Change Phone number using StringSession]

I will add more features Later 😅
"""

keyboard = [
    [
        Button.inline("A", data="Ahack"),
        Button.inline("B", data="Bhack"),
        Button.inline("C", data="Chack"),
        Button.inline("D", data="Dhack"),
        Button.inline("E", data="Ehack"),
    ],
    [
        Button.inline("F", data="Fhack"),
        Button.inline("G", data="Ghack"),
        Button.inline("H", data="Hhack"),
        Button.inline("I", data="Ihack"),
        Button.inline("J", data="Jhack"),
    ],
    [
        Button.inline("K", data="Khack"),
        Button.inline("L", data="Lhack"),
        Button.inline("M", data="Mhack"),
    ],
    [Button.inline("Back", data="osg")],
]


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hack")))
async def start(event):
    global menu
    if event.query.user_id == bot.uid:
        await event.delete()
        async with tgbot.conversation(event.chat_id) as x:
            await x.send_message(
                f"Choose what you want with string session \n\n{menu}", buttons=keyboard
            )
    else:
        await event.answer(
            "U Dont Have Right To Access This Hack Button", cache_time=0, alert=True
        )


bot.loop.run_until_complete(module())
bot.loop.run_until_complete(addons())
bot.loop.run_until_complete(abuses())
bot.loop.run_until_complete(spams())
bot.loop.run_until_complete(assistants())
bot.loop.create_task(hekp())
bot.loop.run_until_complete(killer())
bot.loop.run_until_complete(install())

print(
    f"""
╔════❰PRO-LEGENDBOT❱═❍⊱❁۪۪
║┣⪼ OWNER - {Config.ALIVE_NAME}
║┣⪼ Group - @LegendBot_Pros
║┣⪼ CREATOR - @Pro_LegendBoy
║┣⪼ PRO-LEGENDBOT - {LEGENDversion}
║┣⪼ ✨ 『🔱🇱 🇪 🇬 🇪 🇳 🇩 🔱』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱"""
)
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

bot.loop.run_until_complete(legends())


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()
