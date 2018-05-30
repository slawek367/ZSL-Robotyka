from flask import Flask, session, redirect, url_for, escape, request, render_template, flash

from database import Database
from profile import Profile
from functools import wraps

app = Flask(__name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['logged_in'] is not True:
            flash('You must be logged in to enter this page!', 'danger')
            return index()
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = Database()
        user_password = db.get_user_password(request.form['username'])[0]
        if request.form['password'] == user_password:
            session['logged_in'] = True
            session['user'] = request.form['username']
            return redirect(url_for('index'))
        else:
            session['logged_in'] = False
            session['user'] = False
            flash('You typed wrong username or password!')
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    db = Database()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        if db.add_account(username, password, email):
            flash('Your account was created succesfully!')
        else:
            flash('Account already exists!')

    return render_template('register.html')

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    #if not session['logged_in']:
    #    return redirect(url_for('index'))

    db = Database()
    user_id = db.get_account(session['user'])[0]
    profile = Profile()
    profile.set_user_data(user_id)
    #profile.print_user_data()

    if request.method == 'POST':
        print(request.form['name'])
        return render_template('settings.html')
    else:
        return render_template('settings.html', profile=profile)


@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    session['user'] = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHfdasfadfdfafadaH!jmN]LWX/,?RT'
    app.run(port=5011, debug=True)