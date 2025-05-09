from flask import Flask, render_template, request, redirect, url_for, session
import pymysql

app = Flask(__name__)
app.secret_key = 'skibidisecretkey'

# Database connection
def get_db_connection(): 
    return pymysql.connect(
        host='10.2.3.56', 
        user='root', 
        password='magnum asinum', 
        database='mygamelistsdb'
    )

# Routes
@app.route('/') # When someone visits the root url the index page will be rendered
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST']) # When someone visits the register url the register page will be loaded
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', 
                      (username, password))
        conn.commit() # Commit the changes to the database
        conn.close() # Close the connection
        return redirect(url_for('login'))
    
    # This return is for GET requests
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST']) # When someone visits the login url the login page will be loaded
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        # Check if user exists
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', # Check if user exists %s is a placeholder
                      (username, password))
        user = cursor.fetchone() # Fetch the user from the database
        conn.close()
        
        if user: # If the user fech is not empty then the user is logged in and sent to the index page.
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index')) 
        
    # If the user was not logged in the login page reloads
    return render_template('login.html')

@app.route('/logout') # When someone visits the logout url they are logged out and sent to the index page
def logout():
    session.clear() # Clear the session
    return redirect(url_for('index'))