from flask import Blueprint, render_template

blueprint = Blueprint('people', __name__, url_prefix='/people')

@blueprint.route('/')
def index():
    title = 'Люди'
    return render_template('people/index.html', title=title)
