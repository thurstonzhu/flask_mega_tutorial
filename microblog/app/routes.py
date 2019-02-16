# Import the app_inst class from the app package
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

# View functions = Python functions that serve as handlers for application routes
# View functions are decorated with @app.route

# Decorators modify functions that follow
# Commonly used to register functions as callbacks
# @app.route creates association between URL and function


@app.route('/')
@app.route('/index')
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    title = 'Sign In'
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    template = render_template('login.html', title=title, form=form)
    return template


