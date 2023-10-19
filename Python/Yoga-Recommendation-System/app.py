from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import numpy as np
import pickle
import re
from joblib import load



dbPath = 'model/modelDB.sav'
chPath = 'model/modelCH.sav'
lcPath = 'model/modelLC.sav'
modelDB = load(dbPath)



modelDB = pickle.load(open(dbPath, 'rb'))
modelCH = pickle.load(open(chPath, 'rb'))
modelLC = pickle.load(open(lcPath, 'rb'))

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pythonlogin'

# Intialize MySQL
mysql = MySQL(app)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)    


# http://localhost:5000/python/logout - this will be the logout page
@app.route('/pythonlogin/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))    


# http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/pythonlogin/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)  


# http://localhost:5000/pythonlogin/home - this will be the home page, only accessible for loggedin users
@app.route('/pythonlogin/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('landing.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

# http://localhost:5000/pythinlogin/profile - this will be the profile page, only accessible for loggedin users
@app.route('/pythonlogin/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/diabetes')
def diabetes():
    return render_template("diabetes.html")

@app.route('/cirrhosis')
def cirrhosis():
    return render_template("cirrhosis.html")

@app.route('/lung-cancer')
def lungCancer():
    return render_template("lung-cancer.html")

@app.route("/pythonlogin/predictDiabetes", methods=["POST", "GET"])
def predictDiabetes():
    if request.method == "POST":

        glu = float(request.form["glucose"])
        bp = float(request.form["bloodpressure"])
        insulin = float(request.form["insulin"])
        bmi = float(request.form["bmi"])
        age = float(request.form["age"])

        data = np.array([glu, bp, insulin, bmi, age])
        data = data.reshape(1, 5) 
        output = modelDB.predict(data)
        output = output.tolist()
        
        return redirect(url_for("diabetes", diabetes=output))    

@app.route("/pythonlogin/predictCirrhosis", methods=["POST", "GET"])
def predictCirrhosis():
    if request.method == "POST":

        age = float(request.form["age"])
        bilirubin = float(request.form["bilirubin"])
        chol = float(request.form["cholestrol"])
        albu = float(request.form["albumin"])
        plate = float(request.form["platelets"])

        data = np.array([age, bilirubin, chol, albu, plate])
        data = data.reshape(1, 5) 

        output = modelCH.predict(data)
        output = output.tolist()
        
        return redirect(url_for("cirrhosis", failureStage=output)) 

@app.route("/pythonlogin/predictLungCancer", methods=["POST", "GET"])
def predictLungCancer():
    if request.method == "POST":

        age = float(request.form["age"])
        smoking = float(request.form["smoking"])
        anxiety = float(request.form["anxiety"])
        chronic = float(request.form["chronic"])
        wheezing = float(request.form["wheezing"])

        data = np.array([age, smoking, anxiety, chronic, wheezing])
        data = data.reshape(1, 5) 

        output = modelLC.predict(data)
        output = output.tolist()
        
        return redirect(url_for("lung-cancer", laungCancer=output))

if __name__ == "__name__":
    app.run(debug=True)    