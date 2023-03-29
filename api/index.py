from flask import Flask
from . kraken_data import getTickerInfo
# add . for finding path when using vercel dev

app = Flask(__name__)

ticker_symbol = 'XBTUSD'
long_symbol = 'XXBTZUSD'

def last_close_price():
    ticker = getTickerInfo(ticker_symbol)
    last_trade_closed = ticker[long_symbol]['c']
    content = "Last Trade Closed Price: " + str(last_trade_closed[0])
    return content


def last_ask_price():
    ticker = getTickerInfo(ticker_symbol)
    last_ask = ticker[long_symbol]['a']
    content = "Last Ask Price: " + str(last_ask[0])
    return content


@app.route('/')
def home():
    return last_ask_price()


@app.route('/about')
def about():
    return 'About'


