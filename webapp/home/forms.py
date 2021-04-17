from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired


class HomePageForm(FlaskForm):
    people = SubmitField('Физические лица', render_kw={'class': 'btn btn-primary'})
    policy = SubmitField('Страховые полисы', render_kw={'class': 'btn btn-primary'})
    company = SubmitField('Компании', render_kw={'class': 'btn btn-primary'})
    address = SubmitField('Адреса', render_kw={'class': 'btn btn-primary'})
    transport = SubmitField('Транспорт', render_kw={'class': 'btn btn-primary'})
    event = SubmitField('Страховые случаи', render_kw={'class': 'btn btn-primary'})
