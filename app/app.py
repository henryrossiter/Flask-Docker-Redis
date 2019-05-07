from Flask import flask, request, jsonify, abort
from redis import StrictRedis
import json
import server

app = Flask(__name__)
data = json.load(open('MSFT.json', 'r'))

@app.route('/price', methods = ['GET'])
def get_all_prices():
    server.add_job('get_price')
    return jsonify([col['Close'] for col in data])

@app.route('/jobs', methods = ['GET'])
def jobs():
    result = server.get_all()
    return jsonify(result)
