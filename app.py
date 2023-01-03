"""
The app module: Flask API application.

The root Flask server application.
"""

from flask import Flask

def create_app(config):
    from SMTP.smtp import mail
    from Auth.auth import jwt, bcrypt
    from Database.database import initalize_db, ma
    from Handler.auth import auth
    from Handler.create import create
    from Handler.search import search
    from Handler.update import update
    from Handler.delete import delete
    from Handler.export import export
    from ScheduledTask.scheduler import scheduler_init_app
    from Utils.startup_tasks import import_snomed_csv
    from flask import request
    import logging

    # Initialise application
    app = Flask(__name__)
    app.config.from_object(config)

    app.config['DEBUG'] = check_debug_arg()

    if not (app.config['DEBUG'] or app.config['TESTING']):
        prod_logging()

    # Routes
    app.register_blueprint(auth)
    app.register_blueprint(create)
    app.register_blueprint(search)
    app.register_blueprint(update)
    app.register_blueprint(delete)
    app.register_blueprint(export)

    # initialize app components
    ma.init_app(app)
    initalize_db(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    if app.config['TESTING'] != True:
        scheduler_init_app(app)
        mail.init_app(app)
        import_snomed_csv(app)

    @app.before_request
    def log_request():
        app.logger.info(f'API call made to: {request.url}')

    return app

if __name__ == '__main__':
    from waitress import serve
    from config import AppConfig
    from Utils.app_args import check_debug_arg, check_admin_arg
    from bootstrap_admin import bootstrap_admin
    from app_logging import prod_logging

    app = create_app(AppConfig)
    bootstrap_admin(app, check_admin_arg())
    
    if app.config['DEBUG']:
        app.run(port = 8080, debug = True, use_reloader=False)
    else:
        app.logger.info('Starting server')
        serve(app, host='127.0.0.1', port = 8080, threads = 1)