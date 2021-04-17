from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField

from webapp.people.models import People
from webapp import db


class PeopleForm(FlaskForm):
    last_name = StringField('Фамилия', render_kw={'class': 'form-control'})
    first_name = StringField('Имя', render_kw={'class': 'form-control'})
    patronymic = StringField('Отчество', render_kw={'class': 'form-control'})
    birth_date = DateField('Дата рождения', render_kw={'class': 'form-control'})
    delete = SubmitField('Удалить', render_kw={'class': 'btn btn-primary'})
    save = SubmitField('Сохранить', render_kw={'class': 'btn btn-primary'})
    prev = SubmitField('Пред.', render_kw={'class': 'btn btn-primary'})
    next = SubmitField('След.', render_kw={'class': 'btn btn-primary'})
