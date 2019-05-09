from flask import Flask, jsonify, request, render_template
import json
import pandas
from pandas.io.json import json_normalize
from hotqueue import HotQueue
import datetime
import redis
from plots import create_figure
import os


# The main Flask app
app = Flask(__name__)

def get_redis_ip():
    ip = os.environ.get('REDIS_IP')
    if ip is None:
        ip = "127.0.0.1"
    return ip

try:
    rd = redis.StrictRedis(host=get_redis_ip(), port=6379, db=0)
    q = HotQueue("queue", host=get_redis_ip(), port=6379, db=1)
    print(rd)
    q.put('hello', 'queue')
    rd.ping()
    print('Connected!')
except Exception as ex:
    print('Error:', ex)
    exit('Failed to connect, terminating.')


# Data from a json file
data = json.load(open('MSFT.json', 'r'))
df = json_normalize(data)
df['Date'] = df['Date'].astype(str)



@app.route('/')
def get_all():
    return df.to_json()

@app.route('/graphs', methods = ['GET'])
def show_plots():
    graph_url1 = create_figure(df['Date'], df['Close'])
    graph_url2 = create_figure(df['Date'], df['Volume'])
    return render_template("graphs.html", graph1 = graph_url1, graph2 = graph_url2)

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

@q.worker
def say_hi(str):
    print('-------')
    print(str)
