from flask import Flask, jsonify, request
import json
import pandas
from pandas.io.json import json_normalize


# The main Flask app
app = Flask(__name__)

# Data from a json file
data = json.load(open('MSFT.json', 'r'))
df = json_normalize(data)
df['Date'] = df['Date'].astype(str)

#convert '/' in dates to '-'
df['Date'] = df['Date'].str.replace('/', '-')

@app.route('/')
def get_all():
    return df.to_json()

@app.route('/price', methods = ['GET'])
def get_all_prices():
    #server.add_job('get_price')
    return df['Close'].to_json()

@app.route('/price/<day>', methods = ['GET'])
def get_price(day):
    #todo - input validation
    day_df = df[df['Date'] == day]
    return day_df['Close'].to_json()

@app.route('/average/<day>', methods = ['GET'])
def get_moving_avg(day):
    #todo - input validation
    price_df = df['Close']
    day_df = df[df['Date'] == day]
    last_price = day_df['Close']
    print(last_price)
    prior_prices = price_df.loc[:last_price]
    last_ten = prior_prices.tail(10)
    return last_ten.mean().to_json()

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
