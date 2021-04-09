from flask import Blueprint, render_template

blueprint = Blueprint('address', __name__, url_prefix='/address')

@blueprint.route('/')
def address():
    title = 'Адреса'
    return render_template('address/index.html', title=title)
