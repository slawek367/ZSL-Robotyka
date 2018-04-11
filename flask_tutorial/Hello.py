#Tutorial: https://www.tutorialspoint.com/flask/flask_application.htm
#Tutorial 2: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
#Bootstrap: https://getbootstrap.com/docs/4.0/getting-started/introduction/
'''
{% ... %} for Statements
{{ ... }} for Expressions to print to the template output
{# ... #} for Comments not included in the template output
# ... ## for Line Statements
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name = name)

@app.route('/index')
def index():
    #return '<html><body><h1>Hello World</h1></body></html>'
    return render_template('index.html')

@app.route('/sensors')
def get_sensors():
    sensor_list = {"sensor1": 50, "sensor2": 60, "sensor3": 65}
    return render_template('sensors.html', sensors = sensor_list)

if __name__ == '__main__':
   app.run(port=5011, debug=True)