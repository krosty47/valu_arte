from app import app
from functools import wraps
from tests.fixtures import fixture_default
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade
import os

class test():
    def database(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if os.path.isfile("test.db"):
                os.remove("test.db")
            app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./test.db"
            app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            db = SQLAlchemy(app)
            migrate = Migrate(app, db)
            with app.app_context():
                    upgrade(directory='migrations', revision='head', sql=False, tag=None)
            fixture_default.FixtureDefault.clear()

            return f(*args, **kwargs)
                
        return decorated_function