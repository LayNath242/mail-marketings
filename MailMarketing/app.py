import asyncio
import os
from dotenv import load_dotenv
from quart import Quart, request, jsonify
from telegram import sendcode, login, logout, sendmsg

load_dotenv()


app = Quart(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route('/sendrequest' , methods=['POST'])
async def sendrequest():
    request_data = await request.get_json()
    new_request = {
        'phone':request_data['phone'],
    }
    p = str(new_request['phone'])
    await sendcode(p)
    return jsonify ({'message': 'code have sent to your telegram success !'}), 200


@app.route('/telegramlogin' , methods=['POST'])
async def telegramlogin():
    request_data = await request.get_json()
    new_request = {
        'phone':request_data['phone'],
        'code':request_data['code']
    }
    p = str(new_request['phone'])
    c = int(new_request['code'])
    await login(p, c)
    return jsonify ({'message': 'login success !'}), 200


@app.route('/telegramlogout' , methods=['POST'])
async def telegramlogout():
    request_data = await request.get_json()
    new_request = {
        'phone':request_data['phone'],
    }
    p = str(new_request['phone'])
    await logout(p)
    return jsonify ({'message': 'logout success !'}), 200


@app.route('/telegrammsg' , methods=['POST'])
async def telegrammsg():
    request_data = await request.get_json()
    new_request = {
        'phone':request_data['phone'],
        'channel':request_data['channel'],
        'msg':request_data['msg'],
    }
    p = str(new_request['phone'])
    c = str(new_request['channel'])
    m = str(new_request['msg'])
    await sendmsg(p,c,m)
    return jsonify ({'message': 'sent message success !'}), 200



if __name__ == "__main__":
    app.run(host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            debug=os.getenv("DEBUG"))

