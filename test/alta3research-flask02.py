#!/user/bin/python3

# Import sqlite3
import sqlite3 as sql

# Import flask
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# Connect to a database named 'music.db'
conn = sql.connect('music.db')
print('Successfully connected to database')

# Create a db table
conn.execute('''CREATE TABLE IF NOT EXISTS ARTIST
        (BAND        TEXT        PRIMARY KEY        NOT NULL,
        CATEGORY     TEXT                           NOT NULL);''')
print('Table created successfully')

# Add records to our db table
conn.execute("INSERT OR IGNORE INTO ARTIST (BAND, CATEGORY) VALUES ('The Black Keys', 'Rock')")
conn.commit()
print('Records created successfully')

cursor = conn.execute("SELECT BAND, CATEGORY FROM ARTIST")
for row in cursor:
    print("BAND = ", row[0])
    print("CATEGORY = ", row[1])
print("Operation done successfully")

# Close the connection
conn.close()
