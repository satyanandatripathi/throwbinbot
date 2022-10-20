from telethon.sync import TelegramClient
from telethon import events, Button
from config import Var
import requests
import json
import time


bot = TelegramClient('bot', Var.api_id, Var.api_hash).start(bot_token=Var.token)


def findStr(strg, st, end):
    return strg[strg.find(st) + len(st) : strg.find(end, strg.find(st) + len(st))]


def post(content):
    url = "https://throwbin.in/api/create"
    data = {
        'api_key': Var.throwbin_api_key,
        'content' : content
    }
    x2 = requests.post(url, data = data)
    res = json.loads(x2.text)
    if res['success']:
        return f"https://throwbin.in/{res['url']}"
    

@bot.on(events.NewMessage(func=lambda e: e.is_private))
async def my_event_handler(event):
    if not event.is_channel:
        if event.text == "/start":
            await bot.send_message(event.chat.id, "**Welcome To Throwbin Bot. \n\nThis Bot will help you to host text online.**") 
            return
        elif "yo" == event.text.lower():
            await event.reply("Yo")
            return
        try:
            if event.document:
                path = await event.download_media(f"temp/{time.time()}.txt")
                f = open(path, 'r')
                text = f.read()
                f.close()
            else:
                text = event.raw_text
            url = post(text)
            if url:
                await event.reply(url, link_preview=False)
            else:
                await bot.send_message(event.chat.id, "Something went wrong.")
        except:
            await bot.send_message(event.chat.id, "Something went wrong.")

print("Bot Started.")
bot.run_until_disconnected()
