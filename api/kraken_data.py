import requests
import json 

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
    print(base_url + "/AssetPairs?pair=" + asset)
    return data['result'][asset]

def getTickerInfo(pair):
    
    resp = requests.get(base_url + '/Ticker?pair='+pair)
    data = resp.json()
    return data['result']

def getOHLCdata():
    resp = requests.get(base_url + '/OHLC?pair=XBTUSD')
    print('getOHLCdata youre inside this method')
    print(base_url + '/OHLC?pair=XBTUSD')
    print('======================== so you know your exiting the print statement')
    data = resp.json()
    return data['result']

def getOrderBook():
    resp = requests.get(base_url + '/Depth?pair=XBTUSD')
    print('getOrderBook youre inside this method')
    print(base_url + '/Depth?pair=XBTUSD')
    print('======================== so you know your exiting the print statement')
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

#Below code is "print" statements versus above code "functions"

if __name__ == "__main__":
    print(getServerTime())

info = getAssetPairs('XXBTZUSD') #Kraken has different symbol for BTC/USD listed as 'XXBTZUSD'
print(info)

ticker = getTickerInfo('XBTUSD')
last_trade_closed = ticker['XXBTZUSD']['c']
print("Last Trade Closed Price: " + str(last_trade_closed[0]))

system_status = getSystemStatus()
print("System Status:", system_status)
ask_price = ticker['XXBTZUSD']['a']

print("ask price: " + str(ask_price[0]))

bid_price = ticker['XXBTZUSD']['b']
print("bid price: " + str(bid_price[0]))

info = getOHLCdata()
print(info)

info = getOrderBook()
print(info)

info = getRecentTrades()
print(info)