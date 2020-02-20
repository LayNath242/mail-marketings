import jinja2
from fastapi_mail import FastMail

# ------------------------------------------------------------------------------------------------


async def render_template(template, context, name=None):
    ''' renders a Jinja template into HTML '''
    templateLoader = jinja2.FileSystemLoader('templates')
    templateEnv = jinja2.Environment(loader=templateLoader)
    templ = templateEnv.get_template(template)
    return templ.render(name=name, context=context)


# ------------------------------------------------------------------------------------------------


async def send_email(
    receiver,
    sender,
    password,
    subject,
    body,
    host,
    port,
        ):
    mail = FastMail(
        email=sender,
        password=password,
        tls=True,
        port=port,
        host=host,
        service="gmail"
        )

    await mail.send_message(
        recipient=receiver,
        subject=subject,
        body=body,
        text_format="html"
        )
