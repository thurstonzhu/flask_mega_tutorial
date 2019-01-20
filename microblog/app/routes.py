# Import the app_inst class from the app package
from app import app_inst
from flask import render_template

# View functions = Python functions that serve as handlers for application routes
# View functions are decorated with @app.route

# Decorators modify functions that follow
# Commonly used to register functions as callbacks
# @app.route creates association between URL and function


@app_inst.route('/')
@app_inst.route('/index')
def index():
    user = { 'username': 'Thurston' }
    title = 'Home'
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Cindy'},
            'body': 'You suck'
        }
    ]
    template = render_template('index.html', title=title, user=user, posts=posts)
    return template
