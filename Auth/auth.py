"""
The authentication module: Authentication for admins.

Provides globals and functionality to support the applications
authentication and encryption needs.
"""

import os, logging
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from app_logging import log

jwt = JWTManager()
bcrypt = Bcrypt()

@log
def reset_jwt(app):
    app.config['JWT_SECRET_KEY'] = os.urandom(24)
    jwt._set_default_configuration_options(app)
    logging.info('Invalidating JWT tokens.')