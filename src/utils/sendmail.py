import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from config.config import Config
import utils

CUR_DIR = os.path.dirname(__file__)
config_start = Config(ENV="development")

# ================================================================================================================
# Send Mail
# ================================================================================================================

# Global variables

smtp_server = 'smtp.chu-brugmann.be'
smtp_port = 25
smtp_username = config_start.get_mail_param()['USER']
smtp_password = config_start.get_mail_param()['PASSWORD']


def sendmail(sender, recipient, subject, body):
    message = f'From: {sender}\nTo: {recipient}\nSubject: {subject}\n\n{body}'

    try:
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.login(smtp_username, smtp_password)
        smtp_connection.sendmail(sender, recipient, message)
        smtp_connection.quit()
        print('Email sent successfully!')
        mailflag = True
    except Exception as e:
        print(f'An error occurred: {e}')
        mailflag = False

    return mailflag


def sendmailhtml(sender, recipient, subject, html):
    message = MIMEMultipart('alternative')
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.attach(MIMEText(html, 'html'))

    try:
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.login(smtp_username, smtp_password)
        smtp_connection.sendmail(sender, recipient, message.as_string())
        smtp_connection.quit()
        print('Email sent successfully!')
        mailflag = True
    except Exception as e:
        print(f'An error occurred: {e}')
        mailflag = False

    return mailflag


def sendmailhtmlwithattach(sender, recipient, subject, html, filename):
    message = MIMEMultipart('alternative')
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.attach(MIMEText(html, 'html'))

    with open(filename, 'rb') as attachment:
        part = MIMEApplication(attachment.read(), Name=filename)
        part['Content-Disposition'] = f'attachment; filename="{filename}"'
        message.attach(part)

    try:
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.login(smtp_username, smtp_password)
        smtp_connection.sendmail(sender, recipient, message.as_string())
        smtp_connection.quit()
        print('Email sent successfully!')
        mailflag = True
    except Exception as e:
        print(f'An error occurred: {e}')
        mailflag = False

    return mailflag


# Main =============================================================================================================
if __name__ == "__main__":

    while True:
        options = ["sendmail",
                   "sendmailhtml",
                   "sendmailhtmlwithattach",
                   "Exit",
                   ]
        title = "utils"
        res = utils.let_user_pick(title, options)
        if options[res] == "Exit":
            break
        choice = options[res]

        if choice == "sendmail":
            sender = 'refid.planb@chu-brugmann.be'
            recipient = 'christian.wyns@chu-brugmann.be'
            subject = 'REFID Test Email'
            body = 'This is a test email sent using Python!'
            mailflag = sendmail(sender, recipient, subject, body)

            print(f"mail: {mailflag}")

        if choice == "sendmailhtml":
            sender = 'refid.planb@chu-brugmann.be'
            recipient = 'christian.wyns@chu-brugmann.be'
            subject = 'REFID Test Email'
            html = '<html><body><h1>This is an HTML email sent using Python!</h1></body></html>'
            mailflag = sendmailhtml(sender, recipient, subject, html)

            print(f"mail: {mailflag}")

        if choice == "sendmailhtmlwithattach":
            sender = 'refid.planb@chu-brugmann.be'
            recipient = 'christian.wyns@chu-brugmann.be'
            subject = 'REFID Test Email'
            html = '<html><body><h1>This is an HTML email sent using Python!</h1></body></html>'
            filename = '../_log/refid_sync.log'
            mailflag = sendmailhtmlwithattach(sender, recipient, subject, html, filename)

            print(f"mail: {mailflag}")

        print(choice)
