import base64
from fastapi import FastAPI, File, Form, UploadFile
from telethon import TelegramClient, sync
app = FastAPI()

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.post("/files/")
async def create_file(
    file: UploadFile = File(...) 
        ):
    fname = file.filename
    if allowed_file(fname):
        print(fname)


# async def sendmsg(image):
#     phone = '+855 882778309'
#     api_id= 1060273
#     api_hash='d5b143b9482b385a081de9f8c39e30c1'
#     client = TelegramClient(phone, api_id, api_hash)
#     await client.connect()
#     await client.send_message(
#     434546486,
#     file=image,
#     )