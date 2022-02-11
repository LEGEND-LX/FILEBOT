from telethon.sync import TelegramClient
from telethon.sessions import StringSession

PYTHONBOT = """
"""
print(PYTHONBOT)
print(
    """String Generator. ==> PYTHONBot. Get Your Api Id & Api Hash From my.telegram.org and fill accordingly.
╭━━━┳╮╱╱╭┳━━━━┳╮╱╭┳━━━┳━╮╱╭╮MR_HACKER
┃╭━╮┃╰╮╭╯┃╭╮╭╮┃┃╱┃┃╭━╮┃┃╰╮┃┃
┃╰━╯┣╮╰╯╭┻╯┃┃╰┫╰━╯┃┃╱┃┃╭╮╰╯┃
┃╭━━╯╰╮╭╯╱╱┃┃╱┃╭━╮┃┃╱┃┃┃╰╮┃┃
┃┃╱╱╱╱┃┃╱╱╱┃┃╱┃┃╱┃┃╰━╯┃┃╱┃┃┃
╰╯╱╱╱╱╰╯╱╱╱╰╯╱╰╯╱╰┻━━━┻╯╱╰━╯
╭━━╮╭━━━┳━━━━╮LEGEND-LX
┃╭╮┃┃╭━╮┃╭╮╭╮┃
┃╰╯╰┫┃╱┃┣╯┃┃╰╯
┃╭━╮┃┃╱┃┃╱┃┃
┃╰━╯┃╰━╯┃╱┃┃
╰━━━┻━━━╯╱╰╯PRAWASH_MALVIYA""")
print("Real stick pythonbot newlock")
APP_ID = int(input("Enter APP ID - "))
API_HASH = input("Enter API HASH - ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as PYTHONBOT:
    print("")
    print("This is your STRING_SESSION. Please Keep It safe.")
    print("")
    print(PYTHONBOT.session.save())
    print("")
    print(
        "You can Get Your String Session In Saved Message of Your Telegram Account. Remember To Make New String Session Whenever You Terminate Sessions."
    )
    omk = PYTHONBOT.send_message("me", f"`{PYTHONBOT.session.save()}`")
    omk.reply(
        "The above is the `PYTHON_STRING` #POWERFUL [PYTHONBOT](https://t.me/Python_Userbot_Support)"
    )
