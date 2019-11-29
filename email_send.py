import smtplib, ssl
from email.message import EmailMessage
from config import get_email_config


def send_email(message):
    try:
        msg = EmailMessage()
        msg.set_content(message)
        msg["From"] = get_email_config()["sender_email"]
        msg["To"] = get_email_config()["receiver_email"]
        msg["Subject"] = get_email_config()["subject"]

        context = ssl.create_default_context()
        server = smtplib.SMTP(
            get_email_config()["smtp_server"],
            int(get_email_config()["smtp_server_port"]),
        )
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(
            get_email_config()["sender_email"], get_email_config()["email_password"]
        )
        server.send_message(msg)
        server.quit()

    except Exception as e:
        pass
        # print(e)
