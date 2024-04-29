from flask import *
from serial import Serial
try:
    ser = Serial('COM7', 9600)
except Exception as err:
    print("error in com7")

app= Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")
if __name__ == '__main__':
    app.run(debug=True)