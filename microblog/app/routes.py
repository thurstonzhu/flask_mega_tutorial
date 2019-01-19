# Import the app class from the app package
from app import app_inst

# View functions = Python functions that serve as handlers for application routes
# View functions are decorated with @app.route

# Decorators modify functions that follow
# Commonly used to register functions as callbacks
# @app.route creates association between URL and function


@app_inst.route('/')
@app_inst.route('/index')
def index():
    return "Hello, World!"
