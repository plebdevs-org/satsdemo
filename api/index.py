from flask import Flask
from . kraken_data import getTickerInfo

app = Flask(__name__)

def last_close_price():
    ticker = getTickerInfo('XBTUSD')
    last_trade_closed = ticker['XXBTZUSD']['c']
    content = "Last Trade Closed Price: " + str(last_trade_closed[0])
    return content

def last_ask_price():
    ticker = getTickerInfo('XBTUSD')
    last_ask = ticker['XXBTZUSD']['a']
    content = "Last Ask Price: " + str(last_ask[0])
    return content


@app.route('/')
def home():
    return last_ask_price()


@app.route('/about')
def about():
    return 'About'


