import os
class AppConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'amt.db3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING  = False

class TestConfig(AppConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING  = True
