# -*- coding:utf-8 -*-
# Run a test server.
import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app
from app.extensions import db

if os.path.exists('.env'):
    print('Importing environment from .env file')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

if os.environ.get('DASHAPP') == 'production':
    app = create_app(os.environ.get("DASHAPP") or 'development')
else:
    app = create_app(os.environ.get("DASHAPP") or 'development')

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def hello():
    """say hello for testing"""
    print('hello')


@manager.command
def recreate_db():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    # print(db)
    # db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def reindex_search():
    '''
    Reindex Whooshee
    '''
    # search.delete_index()
    # search.create_index(update=True)

    pass


@manager.command
def test():
    """Run unit tests."""
    tests = unittest.TestLoader().discover('app.tests', pattern='*.py')
    unittest.TextTestRunner(verbosity=1).run(tests)


@manager.command
def dev():
    # TODO add TestingConfig
    db.create_all()
    pass


@manager.command
def refresh_redis_cache():
    """ Refresh Redis Cache Data! """
    pass


if __name__ == '__main__':
    manager.run()
