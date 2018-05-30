from flask import Flask, session, redirect, url_for, escape, request, render_template, flash
from database import Database

app = Flask(__name__)

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
def settings():
    db = Database()
    if request.method == 'POST':
        pass
    else:
        return render_template('settings.html')


@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    session['user'] = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHfdasfadfdfafadaH!jmN]LWX/,?RT'
    app.run(port=5011, debug=True)