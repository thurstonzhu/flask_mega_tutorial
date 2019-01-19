# Directory with an __init__.py is considered a package that can be imported

from flask import Flask

# Create the app object as instance of class Flask imported from package flask
app_inst = Flask(__name__)

# Workaround to circular imports
# app (module)
from app import routes
