import os
import time
import json
import uvicorn
from fastapi import FastAPI
from fastapi import File, UploadFile
from starlette.middleware.cors import CORSMiddleware

from telegram import sendcode, login, logout, getTelegrammember
from telegram import sendcsvmsg, sendmsg


from msgemail import render_template, send_email
from util import allowed_image, allowed_csv, save_file
# -----------------------------------------------------------------------------------------
app = FastAPI()
# -----------------------------------------------------------------------------------------
origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)
# -----------------------------------------------------------------------------------------


@app.post('/sendrequest')
async def sendrequest(phone: str):
    await sendcode(phone)
    return {'message': 'code have sent to your telegram success !'}
# -----------------------------------------------------------------------------------------


@app.post('/telegramlogin')
async def telegramlogin(phone: str, code: int):
    await login(phone, code)
    return {'message': 'login success !'}
# -----------------------------------------------------------------------------------------


@app.post('/telegramlogout')
async def telegramlogout(phone: str):
    await logout(phone)
    return {'message': 'logout success !'}
# -----------------------------------------------------------------------------------------


# @app.post('/telegrammsg')
# async def telegrammsg(
#     phone: str,
#     channel: str,
#     msg: str,
#     image: str = None,
#         ):
#     if image is not None:
#         image = "image/"+image
#     await sendmsg(phone, channel, msg, image)
#     return {'message': 'sent message success !'}
# -----------------------------------------------------------------------------------------


@app.post('/telegramcsv')
async def telegramcsv(
    phone: str,
    channel: str,
    msg: str,
    filename: str,
):
    await sendcsvmsg(phone, channel, msg, filename)
    return {'message': 'sent message success !'}
# -----------------------------------------------------------------------------------------


@app.post('/telegramscraping')
async def telegrammember(phone: str, channel: str, filename: str):
    await getTelegrammember(phone, channel, filename)
    return {'message': 'Scraping is success !'}
# -----------------------------------------------------------------------------------------


@app.post("/telegrammsg/")
async def telegrammsg(
    phone: str,
    channel: str,
    msg: str = None,
    file: UploadFile = File(default="None")
):
    if file == "None":
        image = None
        await sendmsg(phone, channel, msg, image)
    else:
        fname = file.filename
        if await allowed_image(fname):
            image = file.file.read()
            await sendmsg(phone, channel, msg, image)
            return {'message': 'sent success !'}
        else:
            return {'message': 'unsupported file type!'}
# -----------------------------------------------------------------------------------------


@app.post("/emailmessage")
async def emailmessage(
    sender: str,
    password: str,
    subject: str,
    context: str,
    port: str = 587,
    host: str = "smtp.gmail.com",
    htmlfile: str = 'base/default.j2',
    file: UploadFile = File(...)
):
    if await allowed_csv(file):
        await save_file(file)
        filename = file.filename
        with open(filename, 'r') as file:
            data = file.read()
        obj = json.loads(data)
        for key in obj:
            name = key['firstname'] + ' ' + key['lastname']
            email = key['email']
            html = await render_template(htmlfile, context, name)
            await send_email(
                receiver=email,
                sender=sender,
                password=password,
                subject=subject,
                body=html,
                host=host,
                port=port
            )
            time.sleep(5)
        os.remove(filename)
        return {'message': 'sent message success !'}
# -----------------------------------------------------------------------------------------


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
