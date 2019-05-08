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

@app.route('/jobs', methods = ['GET'])
def jobs():
    #result = server.get_all()
    return jsonify(result)
