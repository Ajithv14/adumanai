#core/views.py

from flask import render_template, request, Blueprint
from flask_login import login_required
from adumanai import mongo
from adumanai.models import Cake

core = Blueprint('core', __name__)

@core.route('/')
def index():
    cakes_data = mongo.db.cakes.find()
    cakes = [Cake.from_dict(cake) for cake in cakes_data]
    print(cakes)
    return render_template('index.html',cakes=cakes)


@core.route('/info')
@login_required
def info():
    return render_template('info.html')