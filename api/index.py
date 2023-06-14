from flask import Flask, jsonify
from kraken_data import get_data

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Bitcoin Data API!'

@app.route('/coingecko/price')
def coingecko_price():
    data = get_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run()
