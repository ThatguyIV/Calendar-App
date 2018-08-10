from flask import Flask, redirect, url_for, render_template, request
from forms import RegistrationForm
import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, email TEXT, password TEXT)')

def user_entry(username, email, password):
    c.execute('INSERT INTO users VALUES(' + username + ', ' + email + ', ' + password + ')')
    conn.commit()
    c.close()
    conn.close()

create_table()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login')
def login():
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user_entry(form.username.data, form.email.data, form.password.data)
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/about')
def about():
    return 'This is the about page'

if __name__ == '__main__':
    app.run(debug=true)
