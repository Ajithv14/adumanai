"""adumanai.users.views"""
from flask import render_template, url_for, flash, request, Blueprint, redirect, session
from flask_login import login_user, logout_user, login_required
from adumanai import mongo, oauth
from adumanai.models import User
from adumanai.users.forms import RegistrationForm, LoginForm

users = Blueprint('users',__name__)

@users.route('/callback')
def auth():
    token = oauth.google.authorize_access_token()
    user_info = token['userinfo']
    user = User.from_dict(
                mongo.db.users.find_one({'email': user_info['email']})
                ) if mongo.db.users.find_one({'email': user_info['email']}
                                             ) is not None else None
    if user is None:
        user = User(user_info['email'], user_info['name'])
        mongo.db.users.insert_one(user.to_dict())
    session['user_info'] = user_info
    login_user(user)
    return redirect(url_for('core.index'))

#login
@users.route('/login', methods=['GET','POST'])
def login():
    """login user"""
    redirect_uri = url_for('users.auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


#logout
@users.route('/logout')
@login_required
def logout():
    """ Logout user """
    logout_user()
    session.pop('user_info', None)
    return redirect(url_for('core.index'))
