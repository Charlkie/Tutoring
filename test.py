import sqlite3
from sqlite3 import OperationalError
from flask import Flask, render_template
import os

cwd = os.getcwd()

database = "sample"
path = cwd+"/"+database+".db"

ispath = os.path.exists(cwd+"/"+database+".db")

if not ispath:
    conn = sqlite3.connect('sample.db')
    c = conn.cursor()

    fd = open(database+'.sql', 'r')
    sqlFile = fd.read()
    fd.close()

    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        c.execute(command)
        conn.commit()

    c.execute("SELECT * FROM users") 
    ans = c.fetchall() 
    print(ans)
else:
    print('file already exists, delete before re-running')

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    render_template('index.html', users=)

if __name__ == "__main__":
    app.run()