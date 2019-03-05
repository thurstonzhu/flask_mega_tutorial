# Directory with an __init__.py is considered a package that can be imported

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create the app object as instance of class Flask imported from package flask
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Workaround to circular imports
# app (module)
from app import routes, models
