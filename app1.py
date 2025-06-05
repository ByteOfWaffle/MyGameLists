from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import pymysql
import bcrypt

app = Flask(__name__)
app.secret_key = 'skibidisecretkey'

# Database connection
def get_db_connection(): 
    return pymysql.connect(
        host='10.2.3.93',
        user='mgl_user',  # User, gave it only neccesairy perms in mariadb
        password='123',
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
        
        # Hash the password before storing
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', 
                      (username, hashed))
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
        # Fetch the hashed password for the user
        cursor.execute('SELECT password FROM users WHERE username = %s', (username,))
        user = cursor.fetchone() # user[0] is the hashed password
        conn.close()
         # If the user fech is not empty then the user is logged in and sent to the index page.
        if user and bcrypt.checkpw(password.encode('utf-8'), user[0].encode('utf-8')):
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index')) 
        
    # If the user was not logged in the login page reloads
    return render_template('login.html')

@app.route('/logout') # When someone visits the logout url they are logged out and sent to the index page
def logout():
    session.clear() # Clear the session / Logs you out
    return redirect(url_for('index'))

@app.route('/game-details')
def game_details():
    return render_template('GameDetails.html')
# This route is for the game details page and handles loading in the game list based on user.
@app.route('/list')
def list(): # When someone visits the list url the list page will be loaded
    # Check if user is logged in and update the list based on the logged-in user If not then redirect to login page
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    user = session['username']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM users WHERE username=%s', (user,))
    user_id = cursor.fetchone()[0]
    cursor.execute('SELECT game_name, status, score FROM userlist WHERE user_id=%s', (user_id,))
    # Row and number means which of the selected values is chosen.
    # e.g.in the SELECT above the first value is game_name so that is row 0
    games = [{'name': row[0], 'status': row[1], 'score': row[2]} for row in cursor.fetchall()] 
    conn.close()
    return render_template('list.html', games=games)

@app.route('/guides')
def guides():
    return render_template('guides.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/cookies')
def cookies():
    return render_template('cookies.html')
# Handles adding a game to the user's list
@app.route('/add-to-list', methods=['POST'])
def add_to_list():
    if not session.get('logged_in'):
        return jsonify({'error': 'Not logged in'}), 401
    data = request.get_json()
    user = session['username']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM users WHERE username=%s', (user,))
    user_id = cursor.fetchone()[0]
    cursor.execute(
        'INSERT INTO userlist (user_id, game_id, game_name, status, score) VALUES (%s, %s, %s, %s, %s)',
        (user_id, data['game_id'], data['game_name'], data['status'], data['score'])
    )
    conn.commit()
    conn.close()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)