from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login')
def login():
    return redirect(url_for('index'))

@app.route('/signup')
def signup():
    return 'This is the signup page'

@app.route('/about')
def about():
    return 'This is the about page'

if __name__ == '__main__':
    app.run(debug=true)
