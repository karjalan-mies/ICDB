from flask import Flask, render_template, flash, redirect, url_for
from flask import current_app
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_migrate import Migrate

from webapp.forms import LoginForm
from webapp.models import db, User


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


    @app.route('/index')
    def index():
        title = 'Банк данных страховой компании'
        return render_template('index.html', title=title)

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = 'Страница авторизации'
        login_form = LoginForm()
        return render_template('login.html', title=title, login_form=login_form)


    @app.route('/process_login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы успешно вошли на сайт')
                return redirect(url_for('index'))

        flash('Не правильное имя пользователя или пароль')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешнь разлогинились')
        return redirect(url_for('index'))


    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет админ!'
        else:
            return 'Ты не админ!'


    @app.route('/people')
    def people():
        title = 'Ввод физических лиц'
        return render_template('people.html', title=title)

    @app.route('/policy')
    def policy():
        title = 'Ввод полисов'
        return render_template('policy.html', title=title)

    @app.route('/organization')
    def organization():
        title = 'Ввод организаций'
        return render_template('organization.html', title=title)

    @app.route('/address')
    def address():
        title = 'Ввод адресов'
        return render_template('address.html', title=title)

    @app.route('/transport')
    def transport():
        title = 'Ввод транспортных средств'
        return render_template('transport.html', title=title)

    @app.route('/event')
    def event():
        title = 'Страховой случай'
        return render_template('event.html', title=title)

    return app