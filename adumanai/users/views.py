"""adumanai.users.views"""
from flask import render_template, url_for, flash, request, Blueprint, redirect
from flask_login import login_user, logout_user
from adumanai import mongo
from adumanai.models import User
from adumanai.users.forms import RegistrationForm, LoginForm

users = Blueprint('users',__name__)

# register
@users.route('/register', methods=['GET','POST'])
def register():
    """signup page"""
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    name=form.name.data,
                    password=form.password.data)
        mongo.db.users.insert_one(user.to_dict())
        flash("Thanks for registration")
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)

#login
@users.route('/login', methods=['GET','POST'])
def login():
    """login user"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.from_dict(
                mongo.db.users.find_one({'email': form.email.data})
                ) if mongo.db.users.find_one({'email': form.email.data}
                                             ) is not None else None
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash("Login Successful")

            next = request.args.get('next')

            if next is None or not next[0] == '/':
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html', form=form)

#logout
@users.route('/logout')
def logout():
    """ Logout user """
    logout_user()
    return redirect(url_for('core.index'))
