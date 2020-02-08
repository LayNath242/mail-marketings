To Create Telegram Api_Hash and Api_Id

    1   Login to your Telegram account(https://my.telegram.org/auth)
        with the phone number of the developer account to use.

    2   Click under API Development tools.

    3   A Create new application window will appear. Fill in your application details.
        There is no  need to enter any URL, and only the first two fields (App title and Short name)
        can currently be changed later.

    4   Click on Create application at the end. Remember that your API hash is secret and Telegram
        won’t let you revoke it. Don’t post it anywhere!

**Note
    More detail  https://docs.telethon.dev/en/latest/basic/signing-in.html


TO Run This app:

    pip install pipenv // use to install python virtual environment
    pipenv shell // use to make new virtual environment (i use python3.6)
    pipenv install -r requirements.txt //install module for this project
    $ cd MailMarketing
    $ export QUART_APP=app:app
    $ quart run


About Telegram Mail Api Route

1.Use to Send Request Code to Telegram
    http://127.0.0.1:5000/sendrequest  [POST]

    {
	"phone": "+855 xxxxxxx"    //+855 for cambodia only
    }

2.Use to Sign in to Telegram
    http://127.0.0.1:5000/telegramlogin  [POST]

    {
	"phone": "+855 xxxxxxx",
	"code" : code     // send to your telegram when Send Request Code
    }

3.Use to Send Message to Telegram group member (you must be admin to get member id)
    http://127.0.0.1:5000//telegrammsg  [POST]

    {
	"phone": "+855 xxxxxxx",
	"channel": "https://t.me/joinchat/xxxxxxxxx",  //your group channel invite link
	"msg": "any message"
    }

4.Use to Logout from Account when not use
    http://127.0.0.1:5000/telegramlogout   [POST]

    {
	"phone": "+855 xxxxxxx"
    }
