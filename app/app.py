from flask import Flask, jsonify, request
import json
import pandas
from pandas.io.json import json_normalize
from hotqueue import HotQueue
import datetime
import redis
import server

server.say_hi()

host = 'localhost'
port = 6379

rd = redis.StrictRedis(host=host, port=port, db=0)
queue = HotQueue("myqueue", host=host, port=port, db=0)

# The main Flask app
app = Flask(__name__)

# Data from a json file
data = json.load(open('MSFT.json', 'r'))
df = json_normalize(data)
df['Date'] = df['Date'].astype(str)

@app.route('/')
def get_all():
    queue.put("hello")
    return df.to_json()

@app.route('/prices', methods = ['GET'])
def get_all_prices():
    #server.add_job('get_price')
    return df['Close'].to_json()

@app.route('/price/<day>', methods = ['GET'])
def get_price(day):
    #todo - input validation
    day_df = df[df['Date'] == day]
    return day_df['Close'].to_json()

@app.route('/average/<date>', methods = ['GET'])
def get_moving_avg(date):
    #todo - input validation
    [month, day, year] = date.split("-")
    sum = 0
    for i in range(len(data)):
        [data_month, data_day, data_year] = data[i]['Date'].split("/")
        if data_month >= month and data_day >= day and data_year >= year:
            break
    for j in range(i-10,i):
        sum = sum + data[j]['Close']
    return jsonify(sum/10)

@app.route('/std', methods = ['GET'])
def get_std():
    price_df = df['Close']
    return price_df.std()

@app.route('/price/<day>', methods = ['POST'])
def set_new_price(day):
    #todo - input validation
    return None

@app.route('/jobs', methods = ['GET'])
def jobs():
    #result = server.get_all()
    return jsonify(result)
