from flask import Blueprint, render_template

blueprint = Blueprint('company', __name__, url_prefix='/company')

@blueprint.route('/')
def company():
    title = 'Компании'
    return render_template('company/index.html', title=title)
