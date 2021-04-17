from flask import Blueprint, render_template

from webapp.transport.models import Transport

blueprint = Blueprint('transport', __name__, url_prefix='/transport')

@blueprint.route('/')
def index():
    title = 'Транспортные средства'
    return render_template('transport/index.html', title=title)