from string import Template
import smtplib
import configparser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_body = template_file.read()
    return Template(template_file_body)


def get_email_credentials(path):
    config = configparser.ConfigParser()
    config.read(path)
    if 'email' not in config:
        print("EMAIL SECTION DOES NOT EXIST!")
    else:
        if 'email' and 'password' not in config['email']:
            print('EMAIL AND PASSOWRD NOT EXIST!')
        else:
            return config['email']['email'], config['email']['password']


def send_email(email, password, template, name):
    msg = MIMEMultipart()  # create a message

    # add in the actual person name to the message template
    message = template.substitute(PERSON=name, TITLE="teste", MESSAGE="TESDE DNVO")

    # setup the parameters of the message
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = template

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s = smtplib.SMTP(host="br1042.hostgator.com.br", port=465)
    s.ehlo()
    s.starttls()
    s.login(email, password)
    s.send_message(msg)
    print("enviado!")
    del msg
