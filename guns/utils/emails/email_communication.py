from guns.utils.emails.email_connection import EmailConnection
from string import Template
import configparser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_body = template_file.read()
    return Template(template_file_body)


def get_email_credentials(path):
    cfg = configparser.ConfigParser()
    cfg.read(path)
    if 'host' and 'email' in cfg:
        return EmailConnection(cfg['host']['host'], cfg['host']['port'], cfg['email']['email'], cfg['email']['password'])


def send_email(connection: EmailConnection, template: Template, name, email, subject, message, to_email):
    msg = MIMEMultipart()

    message = template.substitute(NAME=name, EMAIL=email, MESSAGE=message)

    msg['From'] = connection.login
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    s = smtplib.SMTP_SSL(connection.host, connection.port)
    s.login(connection.login, connection.password)
    s.send_message(msg)
    print('ENVIADO!')
    del msg
