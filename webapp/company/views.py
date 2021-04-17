from flask import Blueprint, flash, redirect, render_template, url_for

from webapp.company.models import Company
from webapp.company.forms import CompanyForm

from webapp import db

blueprint = Blueprint('company', __name__, url_prefix='/company')

@blueprint.route('/')
def index():
    title = 'Работа с записями таблицы: "Компании"'
    company_form = CompanyForm()
    return render_template('company/index.html', title=title, company_form=company_form)

@blueprint.route('/process_save', methods=['POST'])
def process_save():
    form = CompanyForm()
    new_company = Company(name=form.name.data, inn=form.inn.data, address=form.address.data, director=form.director.data)
    db.session.add(new_company)
    db.session.commit()
    flash('Изменеия сохранены в банке данных')
    return redirect(url_for('company.index'))

