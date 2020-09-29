from flask import render_template

from views import user_blu


@user_blu.route('/login')
def login():
    return render_template('Login.html')


@user_blu.route('/register')
def register():
    return render_template('Registered.html')
