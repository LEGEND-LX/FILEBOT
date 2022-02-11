from telethon.sync import TelegramClient
from telethon.sessions import StringSession

DRAGONBOT = """
"""
print(DRAGONBOT)
print(
    """String Generator. ==> DRAGONBot. Get Your Api Id & Api Hash From my.telegram.org and fill accordingly.
╭━━━┳╮╱╱╭┳━━━━┳╮╱╭┳━━━┳━╮╱╭╮MR_HACKER
┃╭━╮┃╰╮╭╯┃╭╮╭╮┃┃╱┃┃╭━╮┃┃╰╮┃┃
┃╰━╯┣╮╰╯╭┻╯┃┃╰┫╰━╯┃┃╱┃┃╭╮╰╯┃
┃╭━━╯╰╮╭╯╱╱┃┃╱┃╭━╮┃┃╱┃┃┃╰╮┃┃
┃┃╱╱╱╱┃┃╱╱╱┃┃╱┃┃╱┃┃╰━╯┃┃╱┃┃┃
╰╯╱╱╱╱╰╯╱╱╱╰╯╱╰╯╱╰┻━━━┻╯╱╰━╯PRAWASH_MALVIYA""")
print("Real stick Dragonbot~Pro newlock")
APP_ID = int(input("Enter APP ID - "))
API_HASH = input("Enter API HASH - ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as DRAGONBOT:
    print("")
    print("This is your STRING_SESSION. Please Keep It safe.")
    print("")
    print(DRAGONBOT.session.save())
    print("")
    print(
        "You can Get Your String Session In Saved Message of Your Telegram Account. Remember To Make New String Session Whenever You Terminate Sessions."
    )
    omk = DRAGONBOT.send_message("me", f"`{DRAGONBOT.session.save()}`")
    omk.reply(
        "The above is the `DRAGON_STRING` #POWERFUL [DRAGONBOT~PRO](https://t.me/DragonPro_UserBot)"
    )
