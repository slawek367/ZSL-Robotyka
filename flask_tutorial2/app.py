from flask import Flask, session, redirect, url_for, escape, request, render_template, flash

from database import Database
from profile import Profile
from functools import wraps

from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)

#PHOTO PART
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'D:\profilowe'
configure_uploads(app, photos)

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
    db = Database()
    user_id = db.get_account(session['user'])[0]
    profile = Profile(user_id)

    if request.method == 'POST':
        profile.name = request.form['name']
        profile.surname = request.form['surname']
        profile.age = request.form['age']
        #TODO
        profile.update_user_data()
        return render_template('settings.html', profile=profile)
    else:
        return render_template('settings.html', profile=profile)


@app.route('/user_photo', methods=['GET', 'POST'])
def user_photo():
    #TODO
    # - add database which will store profile photo name and user id
    # - update profile photo on page
    #some instruction: https://stackoverflow.com/questions/44926465/upload-image-in-flask
    print(request.files)
    print(request.method)
    if request.method == 'POST' and 'profile_photo' in request.files:
        filename = photos.save(request.files['profile_photo'])
        return filename
    return redirect(url_for('settings'))


@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    session['user'] = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHfdasfadfdfafadaH!jmN]LWX/,?RT'
    app.run(port=5011, debug=True)