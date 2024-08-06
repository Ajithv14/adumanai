""" Entry point of the app"""
from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager
from authlib.integrations.flask_client import OAuth

from config import Config


app = Flask(__name__)


##### Database setup #########

app.config.from_object(Config)
mongo = PyMongo(app)

##############################

##### Login Configs ##########
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

#############################


oauth = OAuth(app)

oauth.register(
    name='google',
    client_id=app.config['GOOGLE_CLIENT_ID'],
    client_secret=app.config['GOOGLE_CLIENT_SECRET'],
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'},
)

oauth = oauth

from adumanai.core.views import core
from adumanai.users.views import users
from adumanai.cakes_posts.views import cakes
from adumanai.error_pages.handlers import error_pages

app.register_blueprint(core)    
app.register_blueprint(users)
app.register_blueprint(cakes)
app.register_blueprint(error_pages)
