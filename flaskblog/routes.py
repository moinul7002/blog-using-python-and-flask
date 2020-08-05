from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app

posts = [
	{
		'author': 'Moinul',
		'title': 'Blog 1',
		'content': 'My First Post',
		'date_posted': 'Jul 30, 2020'

	},
	{
		'author': 'Fariha',
		'title': 'Blog 2',
		'content': 'My First Post',
		'date_posted': 'Jul 31, 2020'
	}

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')


@app.route('/register', methods = ['GET', 'POST']) #submits a POST request to the same route, so to accept POST request, we need to add a list of allowed methods (GET, POST)
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account has been created for {form.username.data}!', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title = 'Registration', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unseccessful. Please check your username and password.', 'danger')
	return render_template('login.html', title = 'Log In', form = form)