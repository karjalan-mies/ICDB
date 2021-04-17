from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from webapp.admin.views import blueprint as admin_blueprint
from webapp.address.views import blueprint as address_blueprint
from webapp.company.views import blueprint as company_blueprint
from webapp.db import db
from webapp.event.views import blueprint as event_blueprint
from webapp.home.views import blueprint as home_blueprint
from webapp.people.views import blueprint as people_blueprint
from webapp.policy.views import blueprint as policy_blueprint
from webapp.transport.views import blueprint as transport_blueprint
from webapp.user.forms import LoginForm
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(address_blueprint)
    app.register_blueprint(company_blueprint)
    app.register_blueprint(event_blueprint)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(people_blueprint)
    app.register_blueprint(policy_blueprint)
    app.register_blueprint(transport_blueprint)
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
