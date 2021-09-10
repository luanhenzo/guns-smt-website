from flask import Blueprint, render_template, request
from guns.utils.emails.email_communication import read_template, get_email_credentials, send_email
from guns import TEMPLATES_FOLDER, INSTANCE_FOLDER
import os

bp = Blueprint('index', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        call_us_values = request.values.to_dict()
        name = call_us_values['your-name']
        email = call_us_values['your-email']
        subject = call_us_values['subject']
        message = call_us_values['message']

        template = read_template(os.path.join(TEMPLATES_FOLDER, r'emails\call_us_form.txt'))
        credentials = get_email_credentials(os.path.join(INSTANCE_FOLDER, r'call_us_mailcred.ini'))
        send_email(credentials, template, name, email, subject, message, credentials.login)

        return render_template('views/index.html')
    else:
        return render_template('views/index.html')
