from flask import render_template, flash, redirect, request, jsonify, url_for
from werkzeug.urls import url_parse
from app import app, db
from app.core_nancy import predict
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User
import json

@app.route('/')
@app.route('/index')
@login_required
def index():

    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    
    return render_template('login.html', title='Log in', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()

    return redirect(url_for('index'))

@app.route('/_chat')
def chat():
    msg = request.args.get('msg', 0)
    result = "NANCY: " + predict(msg)
    return jsonify(result) #predict(msg)
    
@app.route('/nancy', methods=['GET', 'POST'])
@login_required
def nancy():
    user = {'username': 'visitor'}
      
    return render_template('nancy.html', title='NANCY', user=user)

#@app.route('/intent')
#def intent():
#    intents = json.loads(open('./app/data/intents_v5.json').read())
    
#    return render_template('intent.html', title='Intent', contents=intents)

@app.route('/animation')
def animation():
    user = {'username': 'Jarvis'}
    posts = [
        {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
        },
        {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('animation.html', title='Animation', user=user, posts=posts)

@app.route('/blog/<int:postID>')
def blog(postID):
    return 'Blog number %d' % postID

@app.route('/music')
def music():
    with open('playlist.txt', 'r', encoding='utf-8') as f:
        contents = f.read()

    return render_template('music.html', title='Music', playlist=eval(contents))
