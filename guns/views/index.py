from flask import Blueprint, render_template, request


bp = Blueprint('index', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        call_us_form = request.values.to_dict()
        return render_template('index.html')
    else:
        return render_template('index.html')
