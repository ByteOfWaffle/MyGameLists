from flask import Flask, render_template
import pymysql

conn = pymysql.connect(
    host='10.2.3.90', 
    user='root', 
    password='magnum asinum', 
    database='mygamelistsdb')

# Create a cursor object
cursor = conn.cursor()

# SQL query to create the table
sql_query = """
CREATE TABLE IF NOT EXISTS testnum4 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);
"""

# Execute the query
cursor.execute(sql_query)

# Commit changes and close the connection
cursor.close()
conn.close()

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
    

