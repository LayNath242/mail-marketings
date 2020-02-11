from telethon import TelegramClient, sync
import os
from dotenv import load_dotenv
import time

#------------------------------------------------------------------------------------------------
load_dotenv()

#------------------------------------------------------------------------------------------------
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

#------------------------------------------------------------------------------------------------
async def sendcode(phone_number):
    client = TelegramClient(phone_number, api_id, api_hash)
    phone = await client.connect()
    if not await client.is_user_authorized():
        phone = await client.send_code_request(phone_number)
        phone_code_hash = phone.phone_code_hash
        f= open(phone_number,"w")
        f.write(phone_code_hash)
        f.close()
    else:
        raise Exception('You already have account')

#------------------------------------------------------------------------------------------------
async def login(phone_number, code):
    f= open(phone_number,"r")
    phone_code_hash = f.read()
    f.close()
    try:
        client = TelegramClient(phone_number, api_id, api_hash)
        await client.connect()
        await client.sign_in(phone_number, code, phone_code_hash=phone_code_hash)
        os.remove(phone_number)
    except:
        raise Exception('Login False')

#------------------------------------------------------------------------------------------------
async def logout(phone_number):
    client = TelegramClient(phone_number, api_id, api_hash)
    await client.connect()
    await client.log_out()

#------------------------------------------------------------------------------------------------
async def sendmsg(phone, channel, message):
    client = TelegramClient(phone, api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
        raise Exception("Please Register First")
    participants = await client.get_participants(channel)

    me = await client.get_me()

    if len(participants):
        for user in participants:
            if me.id==user.id:
                pass
            else:
                await client.send_message(user.id,  message=message)
                time.sleep(5)