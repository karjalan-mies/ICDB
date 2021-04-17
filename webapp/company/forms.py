from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField

from webapp.people.models import People
from webapp import db


class CompanyForm(FlaskForm):
    name = StringField('Название', render_kw={'class': 'form-control'})
    inn = StringField('ИНН', render_kw={'class': 'form-control'})
    address = StringField('Адрес', render_kw={'class': 'form-control'})
    director = DateField('Руководитель', render_kw={'class': 'form-control'})
    delete = SubmitField('Удалить', render_kw={'class': 'btn btn-primary'})
    save = SubmitField('Сохранить', render_kw={'class': 'btn btn-primary'})
    prev = SubmitField('Пред.', render_kw={'class': 'btn btn-primary'})
    next = SubmitField('След.', render_kw={'class': 'btn btn-primary'})
