from flask import Blueprint, render_template

blueprint = Blueprint('transport', __name__, url_prefix='/transport')

@blueprint.route('/')
def transport():
    title = 'Транспортные средства'
    return render_template('transport/index.html', title=title)