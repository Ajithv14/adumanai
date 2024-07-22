#core/views.py

from flask import render_template, request, Blueprint
from flask_login import login_required

core = Blueprint('core', __name__)

@core.route('/')
def index():
    return render_template('index.html')


@core.route('/info')
@login_required
def info():
    return render_template('info.html')