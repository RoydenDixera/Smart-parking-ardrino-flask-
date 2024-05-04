from flask import *
from serial import Serial,SerialException
from collections import deque

app = Flask(__name__)

# Initialize serial communication
try:
    ser = Serial('COM7', 9600)
except SerialException as e:
    # Handle serial port initialization error
    print("Error initializing serial port:", e)
    ser = None  # Set ser to None to indicate initialization failure

# Define a deque to store the last three data entries
data_queue = deque(maxlen=3)

# Define a route to get the serial data as JSON
@app.route('/data')
def get_data():
    if ser is not None:
        try:
            while ser.in_waiting > 0:
                # Read data from the serial port
                data = ser.readline().decode()
                data_queue.append(data.strip())  # Append each line of data to the deque
        except SerialException as e:
            # Handle serial communication error
            print("Error reading serial data:", e)
    else:
        # Serial port is not initialized, return empty data
        print("Serial port is not initialized.")
    
    # Return the last three data entries as JSON
    return jsonify(list(data_queue))

# Define a route to render the template
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
