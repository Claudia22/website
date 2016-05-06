from flask import Flask
from flask import render_template
import os
from flask import request
from flask import redirect


app = Flask(__name__)
app.debug = True


import sqlite3
from flask import g

DATABASE = './database.db'


def connect_to_database():
    db = sqlite3.connect(DATABASE)
    
    with db:
        db.execute('CREATE TABLE if not exists messages(pkey integer primary key, firstname,lastname,company,email,message)')
    return db

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
@app.route('/Home.html')
def Home():
    return render_template('Home.html')


@app.route('/About.html')
def About():
    return render_template('About.html')

@app.route('/Contact.html', methods=['GET', 'POST'])
def Contact():
    
    if request.method == 'GET':
        return render_template('Contact.html')

    firstname = request.form['firstname']
    lastname = request.form['lastname']
    company = request.form['company']
    email = request.form['email']
    message = request.form['message']
    

    db = get_db()
    
    with db:
        db.execute('INSERT INTO messages(firstname,lastname,company, email, message)VALUES(?,?,?,?,?)', (firstname,lastname,email,country,comment))

    return redirect('ThankYou.html')


@app.route('/ThankYou.html')
def ThankYou():
    return render_template('ThankYou.html')
@app.route('/Home.html')
def Cv():
    return render_template('Home.html')

@app.route('/About.html')
def Portfolio():
    return render_template('About.html')

@app.route('/Services.html')
def Reflection():
    return render_template('Services.html')

@app.route('/Testemonials.html')
def Reflection():
    return render_template('Testemonials.html')






if __name__ == '__main__':
    # http://damyanon.net/getting-started-with-flask-on-cloud9/
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))