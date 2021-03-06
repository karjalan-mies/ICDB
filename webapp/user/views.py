from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user

from webapp import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    title = 'Страница авторизации'
    login_form = LoginForm()
    return render_template('user/login.html', title=title, login_form=login_form)


@blueprint.route('/process_login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы успешно вошли на сайт')
            return redirect(url_for('home.index'))

    flash('Не правильное имя пользователя или пароль')
    return redirect(url_for('home.index'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешнь разлогинились')
    return redirect(url_for('home.index'))

