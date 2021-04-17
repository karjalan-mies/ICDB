from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user

from webapp.home.forms import HomePageForm

blueprint = Blueprint('home', __name__)#, url_prefix='/home')


@blueprint.route('/')
def index():
    if current_user.is_authenticated:
        home_page_form = HomePageForm()
        title = 'Банк данных страховой компании'
        return render_template('home/index.html', title=title, home_page_form=home_page_form)
    else:
        return redirect(url_for('user.login'))
