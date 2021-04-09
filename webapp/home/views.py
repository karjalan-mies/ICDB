from flask import Blueprint, render_template

blueprint = Blueprint('home', __name__,)

@blueprint.route('/')
@blueprint.route('/index')
def home():
    title = 'Банк данных страховой компании'
    return render_template('home/index.html', title=title)
