import os, time, json
from dotenv import load_dotenv
from quart import Quart, request, jsonify
from telegram import sendcode, login, logout, sendmsg
from msgemail import render_template, send_email

#-----------------------------------------------------------------------------------------
app = Quart(__name__)
app.secret_key = os.getenv("SECRET_KEY")

#-----------------------------------------------------------------------------------------

@app.route('/sendrequest' , methods=['POST'])
async def sendrequest():
    request_data = await request.get_json()
    new_request = {
        'phone':request_data['phone'],
    }
    p = str(new_request['phone'])
    await sendcode(p)
    return jsonify ({'message': 'code have sent to your telegram success !'}), 200

#-----------------------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------------------

@app.route('/telegramlogout' , methods=['POST'])
async def telegramlogout():
    request_data = await request.get_json()
    new_request = {
        'phone':request_data['phone'],
    }
    p = str(new_request['phone'])
    await logout(p)
    return jsonify ({'message': 'logout success !'}), 200

#-----------------------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------------------

@app.route("/emailmessage" , methods=["POST"])
async def emailmessage():
    request_data = await request.get_json(silent=True)
    sender = request_data["sender"]
    password =request_data["password"]
    subject = request_data["subject"]
    context = request_data["context"]

    port = os.getenv("EMAIL_PORT")
    if 'port' in request_data:
        port = request_data['port']

    htmlfile = 'base/default.j2'
    if 'htmlfile' in request_data:
        htmlfile = request_data['htmlfile']

    host = os.getenv("EMAIL_HOST")
    if 'host' in request_data:
        host = request_data['host']

    receiver = None
    if 'receiver' in request_data:
        receiver = request_data['receiver']

    emailfile = 'email-list.json'
    if 'emailfile' in request_data:
        emailfile = request_data['emailfile']

    if receiver is None:
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        with open(ROOT_DIR + '/emailLst/'+emailfile, 'r') as file:
            data=file.read()
        obj = json.loads(data)

        for key in obj:
            name = key['firstname'] +' '+ key['lastname']
            email = key['email']
            html = await render_template(htmlfile, context, name)
            await send_email(receiver=email,
                        sender=sender,
                        password=password,
                        subject=subject,
                        body=html,
                        host=host,
                        port=port)
            time.sleep(5)
    else:
        html = await render_template(htmlfile, context)
        await send_email(receiver=receiver,
                        sender=sender,
                        password=password,
                        subject=subject,
                        body=html,
                        host=host,
                        port=port)
    return jsonify ({"message": "sent message success !"}), 200

#-----------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            debug=os.getenv("DEBUG"))

