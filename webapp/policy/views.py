from flask import Blueprint, render_template

blueprint = Blueprint('policy', __name__, url_prefix='/policy')

@blueprint.route('/')
def index():
    title = 'Страховой полис'
    return render_template('policy/index.html', title=title)
