from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField

from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User

class AdministrationForm(FlaskForm):
    submit = SubmitField('Регистрация пользователей', render_kw={'class': 'form-control'})
    submit_copy = SubmitField('Копирование банка', render_kw={'class': 'form-control'})
    submit_index = SubmitField('Работа с индексами', render_kw={'class': 'form-control'})

class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={'class': 'form-control'})
    email = StringField('Электронная почта', validators=[DataRequired(), Email()],
                        render_kw={'class': 'form-control'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')],
                              render_kw={'class': 'form-control'})
    role = StringField('Роль', render_kw={'class': 'form-control'})
    submit = SubmitField('Отправить!', render_kw={'class': 'btn btn-primary'})

    def validate_username(self, username):
        user_count = User.query.filter_by(username=username.data).count()
        if user_count > 0:
            raise ValidationError('Пользователь с таким именем уже существует')

    def validate_email(self, email):
        user_count = User.query.filter_by(email=email.data).count()
        if user_count > 0:
            raise ValidationError(f'Пользователь с email: {email} уже существует')
