from flask import Blueprint, render_template

from webapp.event.models import InsuranceEvent

blueprint = Blueprint('event', __name__, url_prefix='/event')

@blueprint.route('/')
def index():
    title = 'Страховые случаи'
    return render_template('event/index.html', title=title)
