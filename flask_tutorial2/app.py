from flask import Flask, session, redirect, url_for, escape, request, render_template, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == "test" and \
                request.form['password'] == "haslo":
            session['logged_in'] = True
            flash('You were successfully logged in')
            return render_template('login.html')
        else:
            session['logged_in'] = False
            flash('You typed wrong username or password!')
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHfdasfadfdfafadaH!jmN]LWX/,?RT'
    app.secret_key = 'A0Zr98j/3yX R~XHfdasfadfdfafadaH!jmN]LWX/,?RT'
    app.run(port=5011, debug=True)