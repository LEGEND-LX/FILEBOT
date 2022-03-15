import asyncio
import html
import os
import random
import re
from math import ceil
from re import compile

from telethon import Button, custom, events, functions, types
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.users import GetFullUserRequest

from userbot import *
from userbot.Config import Config
from userbot.helpers.ffunctions.utils import get_readable_time

from . import *

DEFAULTUSER = alive_name = Config.ALIVE_NAME
legend_row = Config.BUTTONS_IN_HELP
legend_emoji1 = Config.HELP_EMOJI1 or "✥"
legend_emoji2 = Config.HELP_EMOJI2 or "✥"
mssge = cstm_pmp = (
    Config.PM_MSG
    or "I am Assistant Of My Owner\nI am Here To Protect My Owner From Scanner"
)
help_pic = Config.HELP_PIC
LOG_GP = Config.LOGGER_ID

PREV_REPLY_MESSAGE = {}
mybot = Config.BOT_USERNAME

HANDLER = os.environ.get("HANDLER", r".")

if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"

USER_BOT_WARN_ZERO = (
    "Enough Of Your Flooding In My Master's PM!! \n\n**🚫 Blocked and Reported**"
)

LEGEND_FIRST = "__{}__\n**Please choose why u are here.** ♥️!!"

about = Config.ALIVE_EMOJI
if about is not None:
    b = about.split()
    c = []
    if len(b) >= 1:
        for d in b:
            c.append(d)
    alive_emoji = random.choice(c)
else:
    alive_emoji = "✥"

alive_txt = (
    os.environ.get("ALIVE_TEMPLATE", None)
    or """
         {}

         {}Bo† Status{}
{} **LegendBo† version:** {}
{} **Telethon version :** {}
{} **Uptime  :** {}
{} **Abuse :** {}
{} **ßudø  :** {}
{} **Bø†  :** {}
"""
)


def button(page, modules):
    Row = legend_row

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(
                    f"{legend_emoji1} " + pair + f" {legend_emoji2}",
                    data=f"Information[{page}]({pair})",
                )
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
                f"⌫ ẞαƈƙ", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(f"🔥 ❌ 🔥", data="close"),
            custom.Button.inline(
                f"ɳ̃êӿ† ⌦", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]

    modules = CMD_HELP


if Config.BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "LEGENDBOT_help":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            HELP_MESSAGE = (
                os.environ.get("HELP_MESSAGE", None)
                or f"『{legend_mention}』\n\n⭐ 𝚃𝚘𝚝𝚊𝚕 𝙼𝚘𝚍𝚞𝚕𝚎𝚜 𝙸𝚗𝚜𝚝𝚊𝚕𝚕𝚎𝚍 ⭆ `{len(CMD_HELP)}`\n🔥 𝚃𝚘𝚝𝚊𝚕 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜⭆ `{len(apn)}`\n📖 Pαցҽ⭆ 1/{veriler[0]}"
            )
            if HELP_MESSAGE:
                b = HELP_MESSAGE.split(", ")
                c = []
                if len(b) >= 1:
                    for d in b:
                        c.append(d)
                help_msg = random.choice(c)
            HELP_PIC = (
                os.environ.get("HELP_PIC", None)
                or "https://te.legra.ph/file/b5d01ceea49ee0a822661.mp4"
            )
            if HELP_PIC is not None:
                b = HELP_PIC.split()
                c = []
                if len(b) >= 1:
                    for d in b:
                        c.append(d)
                help_pic = random.choice(c)
            if help_pic and help_pic.endswith((".jpg", ".png")):
                result = builder.photo(
                    help_pic,
                    text=help_msg,
                    buttons=veriler[1],
                    link_preview=False,
                )
            elif help_pic:
                result = builder.document(
                    help_pic,
                    text=help_msg,
                    title="Help Menu",
                    buttons=veriler[1],
                    link_preview=False,
                )
            else:
                result = builder.article(
                    text="Check Group Inline Permission Or",
                    title="LegendBot Alive",
                    buttons=veriler[1],
                    link_preview=False,
                )
        elif event.query.user_id == bot.uid and query == "alive":
            uptime = get_readable_time((time.time() - StartTime))
            uptime = uptime
            ALIVE_PIC = Config.ALIVE_PIC
            if ALIVE_PIC is not None:
                b = ALIVE_PIC.split()
                c = []
                if len(b) >= 1:
                    for d in b:
                        c.append(d)
                ALV_PIC = random.choice(c)
            else:
                ALV_PIC = "https://telegra.ph/file/af51de2749a4506d3eb43.jpg"
            pp = Config.ALIVE_MSG
            if pp is not None:
                b = pp.split(", ")
                c = []
                if len(b) >= 1:
                    for d in b:
                        c.append(d)
                Msg = random.choice(c)
            else:
                Msg = " Pro LegendBot Is Up"
            leg_end = alive_txt.format(
                Msg,
                alive_emoji,
                alive_emoji,
                alive_emoji,
                LEGENDversion,
                alive_emoji,
                version.__version__,
                alive_emoji,
                uptime,
                alive_emoji,
                abuse_m,
                alive_emoji,
                is_sudo,
                alive_emoji,
                Config.BOY_OR_GIRL,
            )
            alv_btn = [
                [
                    Button.url(
                        f"{LEGEND_USER}", f"tg://openmessage?user_id={Pro_Userboy}"
                    )
                ],
                [
                    Button.url("My Channel", f"https://t.me/{my_channel}"),
                    Button.url("My Group", f"https://t.me/{my_group}"),
                ],
            ]
            if ALV_PIC and ALV_PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALV_PIC,
                    text=leg_end,
                    buttons=alv_btn,
                    link_preview=False,
                )
            elif ALV_PIC:
                result = builder.document(
                    ALV_PIC,
                    text=leg_end,
                    title="LegendBot Alive",
                    buttons=alv_btn,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    text=leg_end,
                    title="LegendBot Alive",
                    buttons=alv_btn,
                    link_preview=False,
                )
        elif event.query.user_id == bot.uid and query == "fsub":
            fsub_btn = [
                [
                    Button.url(
                        f"{LEGEND_USER}", f"tg://openmessage?user_id={Pro_Userboy}"
                    )
                ],
                [
                    Button.url("📍My Channel📍", f"https://t.me/{my_channel}"),
                    Button.url("💝My Group💝", f"https://t.me/{my_group}"),
                ],
            ]
            ALIVE_PIC = Config.ALIVE_PIC
            if ALIVE_PIC is not None:
                b = ALIVE_PIC.split()
                c = []
                if len(b) >= 1:
                    for d in b:
                        c.append(d)
                ALV_PIC = random.choice(c)
            else:
                ALV_PIC = "https://telegra.ph/file/af51de2749a4506d3eb43.jpg"
            if ALV_PIC and ALV_PIC.endswith((".jpg", ".png")):
                result = builder.article(
                    buttons=fsub_btn,
                    link_preview=False,
                )
            elif ALV_PIC:
                result = builder.document(
                    buttons=fsub_btn,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    buttons=alv_btn,
                    link_preview=False,
                )
        elif event.query.user_id == bot.uid and query == "pm_warn":
            lege_nd = LEGEND_FIRST.format(mssge)
            PM_PIC = Config.PM_PIC
            if PM_PIC is not None:
                b = PM_PIC.split()
                c = []
                if len(b) >= 1:
                    for d in b:
                        c.append(d)
                legend_pic = random.choice(c)
            else:
                legend_pic = "https://te.legra.ph/file/0c605739ddaa472cad75f.jpg"
            result = builder.photo(
                file=legend_pic,
                text=lege_nd,
                buttons=[
                    [
                        custom.Button.inline("📝 Request 📝", data="req"),
                        custom.Button.inline("💬 Chat 💬", data="chat"),
                    ],
                    [custom.Button.inline("🚫 Spam 🚫", data="heheboi")],
                    [custom.Button.inline("Curious ❓", data="pmclick")],
                ],
            )
        elif event.query.user_id == bot.uid and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"**⚜ Legendary Af Pro - LegendBot ⚜**",
                buttons=[
                    [Button.url("♥️ Tutorial ♥", "https://youtu.be/9dQgdUJfk_k")],
                    [Button.url("📍 𝚁𝚎𝚙𝚘 📍", "https://github.com/PROBOY-OP/LegendBot")],
                    [
                        Button.url(
                            "💞 Deploy 💞",
                            "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FPROBOY-OP%2FPRO-LEGENDBOT&template=https%3A%2F%2Fgithub.com%2FPROBOY-OP%2FPRO-LEGENDBOT",
                        )
                    ],
                ],
            )
        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )
        else:
            buttons = [
                (
                    Button.url("Sources", "https://github.com/PROBOY-OP/PRO-LEGENDBOT"),
                    Button.url(
                        "Deploy",
                        "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FPROBOY-OP%2FPRO-LEGENDBOT&template=https%3A%2F%2Fgithub.com%2FPROBOY-OP%2FPRO-LEGENDBOT",
                    ),
                )
            ]
            ALIVE_PIC = Config.ALIVE_PIC
            if ALIVE_PIC is not None:
                b = ALIVE_PIC.split()
                c = []
                if len(b) >= 1:
                    for d in b:
                        c.append(d)
                ALV_PIC = random.choice(c)
            else:
                ALV_PIC = "https://telegra.ph/file/af51de2749a4506d3eb43.jpg"
            markup = event.client.build_reply_markup(buttons)
            photo = types.InputWebDocument(
                url=ALV_PIC, size=0, mime_type="image/jpeg", attributes=[]
            )
            text, msg_entities = await event.client._parse_message_text(
                "𝗗𝗘𝗣𝗟𝗢𝗬 𝗬𝗢𝗨𝗥 𝗢𝗪𝗡 𝗣𝗥𝗢 𝗟𝗘𝗚𝗘𝗡𝗗 𝗕𝗢𝗧", "md"
            )
            result = types.InputBotInlineResult(
                id=str(uuid4()),
                type="photo",
                title="LEGENDBOT",
                description="Deploy yourself",
                url="https://github.com/PROBOY-OP/PRO-USERBOT",
                thumb=photo,
                content=photo,
                send_message=types.InputBotInlineMessageMediaAuto(
                    reply_markup=markup, message=text, entities=msg_entities
                ),
            )
        await event.answer([result] if result else None)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"pmclick")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for Other Users..."
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"🔰 This is Pro-Lêɠêɳ̃dẞø† PM Security for {legend_mention} to keep away unwanted retards from spamming PM..."
            )

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"req")))
    async def on_pm_click(legend):
        if legend.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master {legend_mention} Im Try To Get Rid Of This Nigga Pls Dont Touch"
            await legend.answer(fck_bit, cache_time=0, alert=True)
            return
        await legend.get_chat()
        legend.query.user_id
        await legend.edit(
            "Oh You Wanna Talk With My Master\n\nPls Wait Dear \n\n**Btw** **You Can Wait For My Master**"
        )
        await asyncio.sleep(2)
        await legend.edit(
            "Which Type Of Request U Want?",
            buttons=[
                [Button.inline("Register", data="school")],
                [Button.inline("As Usual", data="tg_okay")],
            ],
        )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"tg_okay")))
    async def yeahbaba(legend):
        if legend.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master.This Is for other users"
            await legend.answer(fck_bit, cache_time=0, alert=True)
        else:
            await legend.edit(
                f"✅ **Request Registered** \n\n{legend_mention} will now decide to talk with u or not\n😐 Till then wait patiently and don't spam!!"
            )
            target = await legend.client(GetFullUserRequest(legend.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = legend.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
                tosend = f"**👀 Hey {legend_mention} !!** \n\n⚜️ You Got A Request From [{first_name}](tg://user?id={ok}) In PM!!"
                await bot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"school")))
    async def yeahbaba(legend):
        if legend.query.user_id == bot.uid:
            fck_bit = f"This Is For Other user"
            await legend.answer(fck_bit, cache_time=0, alert=True)
        else:
            await legend.edit(
                f"✅ **Request Registered** \n\n{legend_mention} will now decide to look for your request or not.\n😐 Till then wait patiently and don't spam!!"
            )
            target = await legend.client(GetFullUserRequest(legend.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = legend.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**👀 Hey {legend_mention} !!** \n\n⚜️ You Got A Request From [{first_name}](tg://user?id={ok}) In PM!!"
            await bot.send_message(LOG_GP, tosend)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"chat")))
    async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Ahh!! You here to do chit-chat!!\n\nPlease wait for {legend_mention} to come. Till then keep patience and don't spam."
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**👀 Hey {legend_mention} !!** \n\n⚜️ You Got A PM from  [{first_name}](tg://user?id={ok})  for random chats!!"
            await bot.send_message(LOG_GP, tosend)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"heheboi")))
    async def on_pm_click(legend):
        if legend.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master{legend_mention} Im Try To Get Rid Of This Nigga Pls Dont Touch"
            await legend.answer(fck_bit, cache_time=0, alert=True)
            return
        await legend.get_chat()
        legend_id = legend.query.user_id
        await legend.edit("Okay let Me Think🤫")
        await asyncio.sleep(2)
        await legend.edit("Okay Giving You A Chance🤨")
        await asyncio.sleep(2)
        await legend.edit(
            "Will You Spam?",
            buttons=[
                [Button.inline("Yes", data="lemme_ban")],
                [Button.inline("No", data="hmm")],
            ],
        )
        await bot.send_message(
            LOG_GP,
            message=f"Hello, Master  [Nibba](tg://user?id={legend_id}). Wants To Request Something.",
            buttons=[Button.url("Contact Him", f"tg://user?id=legend_id")],
        )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hmm")))
    async def yes_ucan(legend):
        if legend.query.user_id == bot.uid:
            lmaoo = "You Are Not Requesting , Lol."
            await legend.answer(lmaoo, cache_time=0, alert=True)
            return
        await legend.get_chat()
        await asyncio.sleep(2)
        legend.query.user_id
        await legend.edit("Okay You Can Wait Till Wait")
        hmmmmm = "Okay Kindly wait  i will inform you"
        await bot.send_message(legend.query.user_id, hmmmmm)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lemme_ban")))
    async def yes_ucan(legend):
        if legend.query.user_id == bot.uid:
            lmaoo = "You Are Not Requesting , Lol."
            await legend.answer(lmaoo, cache_time=0, alert=True)
            return
        await legend.get_chat()
        await asyncio.sleep(2)
        legend_id = legend.query.user_id
        await legend.edit("Get Lost Retard")
        ban = f"Pahli Fursat Me Nikal\nU Are Blocked"
        await bot.send_message(legend.query.user_id, ban)
        await bot(functions.contacts.BlockRequest(legend.query.user_id))
        await bot.send_message(
            LOG_GP,
            message=f"Hello, Master  [Nibba](tg://user?id={legend_id}). Has Been Blocked Due to Choose Spam",
            buttons=[Button.url("Contact Him", f"tg://user?id=legend_id")],
        )

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"unmute")))
    async def on_pm_click(event):
        hunter = (event.data_match.group(2)).decode("UTF-8")
        legend = hunter.split("+")
        if not event.sender_id == int(legend[0]):
            return await event.answer("This Ain't For You!!", alert=True)
        try:
            await bot(GetParticipantRequest(int(legend[1]), int(legend[0])))
        except UserNotParticipantError:
            return await event.answer("You need to join the channel first.", alert=True)
        await bot.edit_permissions(
            event.chat_id, int(legend[0]), send_message=True, until_date=None
        )
        await event.edit("Yay! You can chat now !!")

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"reopen")))
    async def reopn(event):
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            current_page_number = 0
            simp = button(current_page_number, CMD_HELP)
            button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            await event.edit(
                f"",
                buttons=simp[1],
                link_preview=False,
            )
        else:
            reply_pop_up_alert = "This Is For My Master Only.Dont Try To Touch Again. Deploy Ur Own ©Pro-Lêɠêɳ̃dẞø†™"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            veriler = custom.Button.inline(
                f"{legend_emoji1} OPEN MENU {legend_emoji2}", data="reopen"
            )
            await event.edit(
                f"My Master {Config.ALIVE_NAME} has Been Closed Menu\n\n               [©️Lêɠêɳ̃dẞø†]({chnl_link})",
                buttons=veriler,
                link_preview=False,
            )
        else:
            await event.answer(
                "Deploy Ur Own     ©Pro-Lêɠêɳ̃dẞø†", cache_time=0, alert=True
            )

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        apn = []
        for x in CMD_LIST.values():
            for y in x:
                apn.append(y)
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                f"{legend_mention}\n\n⭐ 𝚃𝚘𝚝𝚊𝚕 𝙼𝚘𝚍𝚞𝚕𝚎𝚜 𝙸𝚗𝚜𝚝𝚊𝚕𝚕𝚎𝚍⭆ `{len(CMD_HELP)}`\n🔥 𝚃𝚘𝚝𝚊𝚕 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜⭆ `{len(apn)}`\n📖 Pαցҽ⭆ 1/{veriler[0]}\n",
                buttons=veriler[1],
                link_preview=False,
            )
        else:
            return await event.answer(
                "Deploy Ur Own  ©Pro-Lêɠêɳ̃dẞø†",
                cache_time=0,
                alert=True,
            )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    f"{alive_emoji} " + cmd[0] + f" {alive_emoji}",
                    data=f"commands[{commands}[{page}]]({cmd[0]})",
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append(
            [
                custom.Button.inline(
                    f"{legend_emoji1} Help Menu {legend_emoji2}", data=f"page({page})"
                )
            ]
        )
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                f"**📗 𝙵𝚒𝚕𝚎 :**  `{commands}`\n**🔢 Total Commands :**  `{len(CMD_HELP_BOT[commands]['commands'])}`",
                buttons=buttons,
                link_preview=False,
            )
        else:
            return await event.answer(
                "Deploy Ur Own. ©Pro-Lêɠêɳ̃dẞø†™",
                cache_time=0,
                alert=True,
            )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")
        result = f"**📗 𝙵𝚒𝚕𝚎 :**  `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += (
                    f"**⚠️ 𝚆𝚊𝚛𝚗𝚒𝚗𝚐 :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
                )
            result += f"**📍 Type :**  {CMD_HELP_BOT[cmd]['info']['type']}\n\n"
        else:
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ 𝚆𝚊𝚛𝚗𝚒𝚗𝚐 :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**📍 Type :**  {CMD_HELP_BOT[cmd]['info']['type']}\n"
            result += f"**ℹ️ 𝙸𝚗𝚏𝚘 :**  {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**🛠 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜 :**  `{HANDLER[:1]}{command['command']}`\n"
        else:
            result += f"**🛠 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜 :**  `{HANDLER[:1]}{command['command']} {command['params']}`\n"
        if command["example"] is None:
            result += f"**💬 𝙴𝚡𝚙𝚕𝚊𝚗𝚊𝚝𝚒𝚘𝚗 :**  `{command['usage']}`\n\n"
        else:
            result += f"**💬 𝙴𝚡𝚙𝚕𝚊𝚗𝚊𝚝𝚒𝚘𝚗 :**  `{command['usage']}`\n"
            result += f"**⌨️ 𝙵𝚘𝚛 𝙴𝚡𝚊𝚖𝚙𝚕𝚎 :**  `{HANDLER[:1]}{command['example']}`\n\n"

        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                result,
                buttons=[
                    custom.Button.inline(
                        f"{legend_emoji1} Return {legend_emoji2}",
                        data=f"Information[{page}]({cmd})",
                    )
                ],
                link_preview=False,
            )
        else:
            return await event.answer(
                "Deploy Ur Own ©Pro-Lêɠêɳ̃dẞø†™ ",
                cache_time=0,
                alert=True,
            )
