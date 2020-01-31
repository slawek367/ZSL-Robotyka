from flask import Flask
from flask import render_template
import sys
from flask import request

sys.path.insert(0, '/home/pi/Desktop/ZSL-Robotyka/led_display')
import screen_1 as lcd

app = Flask(__name__)

@app.route('/')
def homepage():
    lcd.screen1.show_message("TEST")
    return render_template("main.html")

@app.route('/show_message', methods=['POST'])
def show_message():
    #lcd.screen1.show_message(str(request.form["text"]))
    lcd.screen1.show_message("TEST")
    print(str(request.form["text"]))
    return "Showing text: "

if __name__ == "__main__":
    app.run()
