from flask import Flask, jsonify, request
import json

# The main Flask app
app = Flask(__name__)

# Data from a json file
data = json.load(open('MSFT.json', 'r'))

@app.route('/')
def get_all():
    return jsonify(data)

@app.route('/price', methods = ['GET'])
def get_all_prices():
    #server.add_job('get_price')
    return jsonify([col['Close'] for col in data])

@app.route('/price/<day>', methods = ['GET'])
def get_price(day):
    return jsonify([col['Close'] for col in data if col['Date'] == day])

@app.route('/average/<day>', methods = ['GET'])
def get_moving_avg(day):
    return jsonify(sum([col['Close'] for col in data[-10:]]) / 10)

@app.route('/std', methods = ['GET'])
def get_std():
    return None

@app.route('/price/<day>', methods = ['POST'])
def set_new_price(day):
    return None

@app.route('/jobs', methods = ['GET'])
def jobs():
    #result = server.get_all()
    return jsonify(result)
