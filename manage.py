import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db
from tests.fixtures import fixture_default
# from tests.fixtures import fixture_default

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def fixture_run():
    fixture_default.FixtureDefault.run()


@manager.command
def fixture_clear():
    fixture_default.FixtureDefault.clear()


if __name__ == '__main__':
    manager.run()
