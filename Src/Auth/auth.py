"""
The authentication module: Authentication for admins.

Provides globals and functionality to support the applications
authentication and encryption needs.
"""

import os, logging
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from Utils.app_logging import log

jwt = JWTManager()
"""JWT management global"""

bcrypt = Bcrypt()
"""Encryption global"""

@log
def reset_jwt(app):
    """
    Resets the Flask applications JWT secret key, in order to revoke all
    currently issued JWT authentication tokens.

    :param app: The current flask application to reset the JWT secret key for
    :type app: Flask applicaton
    """
    app.config['JWT_SECRET_KEY'] = os.urandom(24)
    jwt._set_default_configuration_options(app)
    logging.info('Invalidating JWT tokens.')