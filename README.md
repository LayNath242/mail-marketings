# Koompi Mail Marketing

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)]()

Koompi Mail Marketing is program use to sent email and sent message to telegram.

## Features!

  - Sent message all group member in Telegram
  - See email to any email in json file
  - This app use python FastApi web framework

## To Run This Python Code

Install the dependencies and virtual environment.
```sh
 $ pip install pipenv  (use to install python virtual environment if you don`t have)
 $ pipenv shell (use to make new virtual environment my project is use python3.6)
 $ pipenv install -r requirements.txt (install module that we need for this project)
```
For start the server
```sh
 - $ cd MailMarketing
 - $ python app.py 
```
- you also can run  $ uvicorn app:app --reload
### To Use Sent Mail In Telegram

Create Telegram Api_Hash and Api_Id :
  - [Login] to your Telegram account
   with the phone number of the developer account to use.
 - Click under API Development tools.
 - A Create new application window will appear. Fill in your application details.
  There is no  need to enter any URL, and only the first two fields (App title and Short name)
  can currently be changed later.
- Click on Create application at the end. Remember that your API hash is secret and Telegram
  won’t let you revoke it. Don’t post it anywhere!

> More detail [Telegram] Api

About My Telegram Route:


| Function | Method | Route |Variable|
| ------ | ------ |------ |------ |
| Send Request Code | POST |http://127.0.0.1:8000/sendrequest |phone
| Sign in | POST |http://127.0.0.1:8000/telegramlogin |phone, code
| Send Message | POST |http://127.0.0.1:8000/telegrammsg |phone, channel, msg
| Log out | POST |http://127.0.0.1:8000/telegramlogout |phone

### To Use Sent Email

Make Your Gmail Enable SMTP Mail

- How to do [watch] this

About My Email Route:


| Function | Method | Route |Require Variable|
| ------ | ------ |------ |------ |
| Send Email | POST |http://127.0.0.1:8000/emailmessage |sender, password, subject, context|

* Note This function have test only with gmail

    * Server: smtp.gmail.com
    * Encryption/Authentication: StartTLS
    * Port: 587

It can sent all message to all email in file in emailLst folder and you can create html template in templates folder

### Note:
    - To test please go to http://127.0.0.1:8000/docs
License
----

GNU General Public License

   [Login]: <https://my.telegram.org/auth>
   [watch]: <https://www.youtube.com/watch?v=D-NYmDWiFjU>
   [Telegram]: <https://docs.telethon.dev/en/latest/basic/signing-in.html>
