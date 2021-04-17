from flask import Blueprint, redirect, url_for, render_template, flash
from flask_login import current_user, login_required

from webapp.db import db
from webapp.admin.forms import RegistrationForm, AdministrationForm
from webapp.user.models import User

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
@blueprint.route('/administration')
@login_required
def admin_index():
    if current_user.is_admin:
        title = 'Панель администрирования'
        administration_form = AdministrationForm()
        return render_template('admin/administration.html', title=title, form=administration_form)
    else:
        return 'Ты не админ!'


@blueprint.route('/register')
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for('news.index'))
    title = 'Страница регистрации'
    register_form = RegistrationForm()
    return render_template('admin/registration.html', title=title, form=register_form)


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role=form.role.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Пользователь успешно зарегистрирован!')
        return redirect(url_for('admin.register'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Ошибка в поле "{getattr(form, field).label.text}" - {error}')
        return redirect(url_for('admin.register'))
