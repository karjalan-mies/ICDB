from flask import Blueprint, render_template

blueprint = Blueprint('event', __name__, url_prefix='/event')

@blueprint.route('/')
def event():
    title = 'Страховые случаи'
    return render_template('event/index.html', title=title)

