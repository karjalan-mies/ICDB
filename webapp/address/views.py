from flask import Blueprint, render_template

from webapp.address.models import Address

blueprint = Blueprint('address', __name__, url_prefix='/address')

@blueprint.route('/')
def index():
    title = 'Адреса'
    return render_template('address/index.html', title=title)
