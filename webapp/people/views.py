from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user

from webapp.people.models import People
from webapp.people.forms import PeopleForm
from webapp import db

blueprint = Blueprint('people', __name__, url_prefix='/people')

@blueprint.route('/')
def index():
    if current_user.is_authenticated:
        title = 'Работа с записями таблицы: "Физические лица"'
        people_form = PeopleForm()
        return render_template('people/index.html', title=title, people_form=people_form)
    else:
        return redirect(url_for('user.login'))

@blueprint.route('/process_save', methods=['POST'])
def process_save():
    form = PeopleForm()
    new_people = People(last_name=form.last_name.data, first_name=form.first_name.data, patronymic=form.patronymic.data,
                        birth_date=form.birth_date.data)
    db.session.add(new_people)
    db.session.commit()
    flash('Изменеия сохранены в банке данных')
    return redirect(url_for('people.index'))
