# referent by https://gist.github.com/perfecto25/4b79b960eb58dc1f6025b56394b51cc1

import smtplib, ssl, os, sys, jinja2
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

ssl._create_default_https_context = ssl._create_unverified_context

async def render_template(template, context, name=None):
    ''' renders a Jinja template into HTML '''
    templateLoader = jinja2.FileSystemLoader('templates')
    templateEnv = jinja2.Environment(loader=templateLoader)
    templ = templateEnv.get_template(template)
    return templ.render(name=name, context=context)
#------------------------------------------------------------------------------------------------

async def send_email(receiver,
                    sender,
                    password,
                    subject,
                    body,
                    host,
                    port,
                    ):

    msg = MIMEMultipart('alternative')
    msg['From']    = sender
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))
    server = smtplib.SMTP(host, port)
    try:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
    except Exception:
        pass
    finally:
        server.quit()

