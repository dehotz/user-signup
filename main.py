from flask import Flask, request, redirect, render_template, url_for
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=['GET', 'POST'])
def index():
	
	if request.method == 'POST':
		return render_template('signup.html', title="Signup", username_error=username_error)
	
	return render_template('signup.html', title="Signup")

@app.route("/validate", methods=['POST'])
def validate():
	username = request.form['username']
	password = request.form['password']
	vpassword = request.form['vpassword']
	email = request.form['email']
	
	username_error = ""
	password_error = ""
	vpassword_error = ""
	email_error = ""
	
	##validation username
	##must not be empty, contain spaces, or be under 3 chars or more than 20
	if username == '':
		username_error = "Please enter a username."
	elif len(username) < 3:
		username_error = "Username must be between 3 and 20 characters long."
	elif len(username) > 20:
		username_error = "Username must be between 3 and 20 characters long."
	elif ' ' in username:
		username_error = "Username must not contain spaces."
	
	##validation password
	##must not be empty, contain spaces, or be under 3 chars or more than 20
	##must match vpassword
	if password == '':
		password_error = "Please enter a password."
	elif len(password) < 3:
		password_error = "Password must be between 3 and 20 characters long."
	elif len(password) > 20:
		password_error = "Password must be between 3 and 20 characters long."
	elif ' ' in password:
		password_error = "Password must not contain spaces."
	elif password != vpassword:
		password_error = "Passwords must match."
	
	##validation email
	##may be empty, but if filled must contain @ and 1 '.'
	if email != '':
		if '@' not in email:
			email_error = "Please enter a proper E-mail address. (Including both an '@' and a '.')"
		elif '.' not in email:
			email_error = "Please enter a proper E-mail address. (Including both an '@' and a '.')"
		elif len(email) < 3:
			email_error = "Please enter a proper E-mail address. (Between 3 and 20 characters)"
		elif len(email) > 20:
			email_error = "Please enter a proper E-mail address. (Between 3 and 20 characters)"
		elif ' ' in email:
			email_error = "Please enter a proper E-mail address. (No spaces)"
		
	#return render_template('welcome.html', username=username, password=password, vpassword=vpassword, email=email)

	##check for any errors, if there then render the signup template but pass it the errors, if not, then redirect welcome
	if not username_error and not email_error and not password_error:
		return render_template('welcome.html', username=username, password=password, vpassword=vpassword, email=email)
		#need to figure out the redirect things
		#return redirect(url_for('/wecome', username=username))
		#return redirect('/welcome?time={0}'.format(time))
	else:
		return render_template('signup.html', title="Signup", username_error=username_error, email_error=email_error, password_error=password_error, username=username, email=email)
	
@app.route("/welcome", methods=['POST'])
def welcome():
	username = request.form['username']
	password = request.form['password']
	vpassword = request.form['vpassword']
	email = request.form['email']
	
	return render_template('welcome.html', username=username, password=password, vpassword=vpassword, email=email)
	
app.run()