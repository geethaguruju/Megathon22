from flask import Flask
from flask_bcrypt import Bcrypt
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from importlib import import_module


bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'



def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    for module_name in ('authentication', 'main'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()



def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    

    return app