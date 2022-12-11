from flask import Flask

def create_app(config):
    from Database.database import initalize_db, ma
    from Handler.auth import auth
    from Handler.create import create
    from Handler.search import search
    from Handler.update import update
    from Handler.delete import delete
    from Handler.export import export
    from ScheduledTask.scheduler import scheduler_init_app
    from Utils.startup_tasks import import_snomed_csv

    # Initialise application
    app = Flask(__name__)
    app.config.from_object(config)

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

    if app.config['TESTING'] != True:
        scheduler_init_app(app)
        import_snomed_csv(app)


    return app

if __name__ == '__main__':
    from config import AppConfig
    app = create_app(AppConfig)
    app.run(port = 8080, debug = True, use_reloader=False)