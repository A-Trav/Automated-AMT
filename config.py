"""
The config module: Application configuration.

Provides different configuration classes to run the Flask application with.
"""

import os

class AppConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'amt.db3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.urandom(24)
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_USE_SSL = True
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    TESTING = False

class TestConfig(AppConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING  = True
