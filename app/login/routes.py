from flask import render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.urls import url_parse

from app import login_manager
from . import login_bp
from .forms import LoginForm
from .models import User, users, get_user

user = User(len(users) + 1, 'asvac', '4sv4c')
users.append(user)

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('equipos.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.user.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('equipos.index'))
    return render_template('login_form.html', form=form)


@login_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('equipos.index'))

