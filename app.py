from flask import Flask, redirect, url_for, render_template, request
from forms import RegistrationForm

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
        user = User(form.username.data, form.email.data, form.password.data)
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/about')
def about():
    return 'This is the about page'

if __name__ == '__main__':
    app.run(debug=true)
