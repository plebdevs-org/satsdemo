import requests

base_url = 'https://api.kraken.com/0/public'

def getServerTime():
    resp = requests.get(base_url + '/Time')
    data = resp.json()
    readable_date = data['result']['rfc1123']
    return readable_date


def getSystemStatus(): 
    resp = requests.get(base_url + '/SystemStatus')
    data = resp.json()
    return data['result']


def getAssetPairs(asset):
    resp = requests.get(base_url + "/AssetPairs?pair=" + asset)
    data = resp.json()
    return data['result'][asset]


def getTickerInfo(pair):
    resp = requests.get(base_url + '/Ticker?pair='+pair)
    data = resp.json()
    return data['result']

def getOHLCdata():
    resp = requests.get(base_url + '/OHLC?pair=XBTUSD')
    data = resp.json()
    return data['result']

def getOrderBook():
    resp = requests.get(base_url + '/Depth?pair=XBTUSD')
    data = resp.json()
    return data['result']

def getRecentTrades():
    resp = requests.get(base_url + '/Trades?pair=XBTUSD')
    data = resp.json()
    return data['result']

def getRecentSpreads():
    resp = requests.get(base_url + '/Spread?pair=XBTUSD')
    data = resp.json()
    return data['result']

if __name__ == "__main__":
    print(getServerTime())

    # Kraken has weird full symbol for BTC/USD as 'XXBTZUSD'
    info = getAssetPairs('XXBTZUSD')
    # print(info)
    
    ticker = getTickerInfo('XBTUSD')
    last_trade_closed = ticker['XXBTZUSD']['c']
    print("Last Trade Closed Price: " + str(last_trade_closed[0]))
    
    ask_price = ticker['XXBTZUSD']['a']
    print("ask price: " + str(ask_price[0]))

    bid_price = ticker['XXBTZUSD']['b']
    print("bid price: " + str(bid_price[0]))
