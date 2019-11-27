import smtplib, ssl
from config import get_config


def send_email(message):
    try:
        smtp_server = get_config()["smtp_server"]
        port = int(get_config()["smtp_server_port"])
        sender_email = get_config()["sender_email"]
        email_password = get_config()["email_password"]
        receiver_email = get_config()["receiver_email"]

        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, email_password)
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        pass
        # print(e)
