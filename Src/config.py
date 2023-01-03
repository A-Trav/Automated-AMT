"""
The config module: Application configuration.

Provides different configuration classes to run the Flask application with.
"""

import os
from os.path import join

class AppConfig:
    """
    AppConfig class represents the Flask applications Development and Deployment configuration settings.
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(os.getcwd(), 'amt.db3')
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
    """
    TestConfig class represents the Flask applications Test configuration settings.

    :param AppConfig: The base application config to inherit configuration settings from
    :type AppConfig: AppConfig
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING  = True
