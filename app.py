from flask import Flask
import os

from Database.database import initalize_db, ma

base_dir = os.path.abspath(os.path.dirname(__file__))

# Initialise application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'amt.db3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize app components
ma.init_app(app)
initalize_db(app)

if __name__ == '__main__':
    app.run(port = 8080, debug = True)