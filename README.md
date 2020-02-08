# Koompi Mail Marketing

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)]()

Koompi Mail Marketing is program use to sent email and sent message to telegram.

## Features!

  - Sent message all group member in Telegram
  - See email to any email in json file

## To Run This Python Code
Install the dependencies and virtual environment.
```sh
 $ pip install pipenv  (use to install python virtual environment)
 $ pipenv shell (use to make new virtual environment my project is use python3.6)
 $ pipenv install -r requirements.txt (install module tha we need for this project)
```
For start the server
```sh
 - $ cd MailMarketing 
 - $ export QUART_APP=app:app
 - $ quart run
```
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
| Send Request Code | POST |[http://127.0.0.1:5000/sendrequest][PlDb] |phone
| Sign in | POST |[http://127.0.0.1:5000/telegramlogin][PlGh] |phone, code
| Send Message | POST |[http://127.0.0.1:5000//telegrammsg][PlGd] |phone, channel, msg
| Log out | POST |[plugins/onedrive/README.md][PlOd] |phone


example:

- 1. Send Request to get code:
    {
	"phone": "+xxx xxxxxxx"
    }
    
     > code will send to your telegram account
- 2. Sign in to Telegram account:
    {
	"phone": "+xxx xxxxxxx",
	"code" : code   
    }
-  3. Send Message to Telegram group:
    {
	"phone": "+855 xxxxxxx",
	"channel": "https://t.me/joinchat/xxxxxxxxx",
	"msg": "any message"
    }
        > channel is your group channel invite link
- 4.  Logout from Tegram account:
    {
	"phone": "+855 xxxxxxx"
    }
    
      > Log out when you not use


### To Use Sent Email 
Make Your Gmail Enable SMTP Mail

- How to do [watch] this

About My Telegram Route:
| Function | Method | Route |Require Variable|
| ------ | ------ |------ |------ |
| Send Email | POST |[http://127.0.0.1:5000/emailmessage][PlDb] |sender, password, subject, context|

* Note This fuction have test only with gmail
    * Server: smtp.gmail.com
    * Encryption/Authentication: StartTLS
    * Port: 587

example :
  -  {
        "sender": "your sender email",
        "password": "your password",
        "subject": "your subject ",
        "context": "message you want to sent"
    }

It can sent all message to all email in file in emailLst floder and you can create html template in templates folder


License
----

GNU General Public License

   [Login]: <https://my.telegram.org/auth>
   [watch]: <https://www.youtube.com/watch?v=D-NYmDWiFjU>
   [Telegram]: <https://docs.telethon.dev/en/latest/basic/signing-in.html>
