from flask import Flask, render_template, jsonify
from serial import Serial
from collections import deque

app = Flask(__name__)

# Create a serial object
ser = Serial("COM7", 9600)

# Define a deque to store the last three data entries
data_queue = deque(maxlen=3)

# Define a route to get the serial data as JSON
@app.route('/data')
def get_data():
    while ser.in_waiting > 0:
        # Read data from the serial port
        data = ser.readline().decode()
        data_queue.append(data.strip())  # Append each line of data to the deque

    # Return the last three data entries as JSON
    return jsonify(list(data_queue))

# Define a route to render the template
@app.route('/')
def index():

    return render_template('dap.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
