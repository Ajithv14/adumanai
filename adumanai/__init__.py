from flask import Flask
from flask_pymongo import PyMongo
from config import Config
from flask_login import LoginManager

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

from adumanai.core.views import core
from adumanai.users.views import users
from adumanai.cakes_posts.views import cakes
from adumanai.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(cakes)
app.register_blueprint(error_pages)
