from fastapi import FastAPI, File, UploadFile
import pandas as pd
import json
import os
import time
from msgemail import render_template, send_email
from util import allowed_csv

app = FastAPI()


async def save_file(file):
    df = pd.read_csv(file.file)
    df.to_json(file.filename, orient='records')


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
        with open(file.filename, 'r') as file:
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
        os.remove(file.filename)
        return {'message': 'sent message success !'}
