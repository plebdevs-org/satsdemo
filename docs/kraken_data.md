```
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
    print('Stay humble stack sats...')
    print(base_url + "/AssetPairs?pair=" + asset)
    print('=========================')
    data = resp.json()
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

if __name__ == "__main__":
    print(getServerTime())

    # Kraken has weird full symbol for BTC/USD as 'XXBTZUSD'
    # info = getAssetPairs('XXBTZUSD')
    # print(info)
    
    # ticker = getTickerInfo('XBTUSD')
    # last_trade_closed = ticker['XXBTZUSD']['c']
    # print("Last Trade Closed Price: " + str(last_trade_closed[0]))
    
    # ask_price = ticker['XXBTZUSD']['a']
    # print("ask price: " + str(ask_price[0]))

    # bid_price = ticker['XXBTZUSD']['b']
    # print("bid price: " + str(bid_price[0]))

    #info = getOHLCdata()
    #print(info)

    #info = getOrderBook()
    #print(info)

    info = getRecentTrades()
    print(info)
```
# The code above demonstrates several functions to interact with the Kraken API:

[getServerTime()] function retrieves the server time from the API.
[getSystemStatus()] function retrieves the system status information from the API.
[getAssetPairs(asset)] function retrieves the asset pairs for a given asset.
[getTickerInfo(pair)] function retrieves ticker information for a specified trading pair.
[getOHLCdata()] function retrieves OHLC (Open, High, Low, Close) data for the XBT/USD pair.
[getOrderBook()] function retrieves the order book data for the XBT/USD pair.
[getRecentTrades()] function retrieves recent trades data for the XBT/USD


```
$ python3 kraken_data.py 
Server Time: Wed, 17 May 23 13:09:17 +0000
System Status: {'status': 'online', 'timestamp': '2023-05-17T13:09:17Z'}
===========================================================================
https://api.kraken.com/0/public/AssetPairs?pair=XXBTZUSD
===========================================================================
{'altname': 'XBTUSD', 'wsname': 'XBT/USD', 'aclass_base': 'currency', 'base': 'XXBT', 'aclass_quote': 'currency', 'quote': 'ZUSD', 'lot': 'unit', 'cost_decimals': 5, 'pair_decimals': 1, 'lot_decimals': 8, 'lot_multiplier': 1, 'leverage_buy': [2, 3, 4, 5], 'leverage_sell': [2, 3, 4, 5], 'fees': [[0, 0.26], [50000, 0.24], [100000, 0.22], [250000, 0.2], [500000, 0.18], [1000000, 0.16], [2500000, 0.14], [5000000, 0.12], [10000000, 0.1]], 'fees_maker': [[0, 0.16], [50000, 0.14], [100000, 0.12], [250000, 0.1], [500000, 0.08], [1000000, 0.06], [2500000, 0.04], [5000000, 0.02], [10000000, 0.0]], 'fee_volume_currency': 'ZUSD', 'margin_call': 80, 'margin_stop': 40, 'ordermin': '0.0001', 'costmin': '0.5', 'tick_size': '0.1', 'status': 'online', 'long_position_limit': 250, 'short_position_limit': 200}
```

The output is the response from the Kraken API when querying the asset pair 'XXBTZUSD' (Bitcoin to US Dollar). Here's a breakdown of the information contained in the response:

Asset Pair Information:
Alternative Name: XBTUSD
WebSocket Name: XBT/USD
Base Asset Class: Currency
Base Asset: XXBT (Bitcoin)
Quote Asset Class: Currency
Quote Asset: ZUSD (US Dollar)
Lot: Unit
Cost Decimals: 5
Pair Decimals: 1
Lot Decimals: 8
Lot Multiplier: 1
Leverage Buy: [2, 3, 4, 5]
Leverage Sell: [2, 3, 4, 5]
Fees: A list of fee tiers based on trading volume. Each tier is represented as [volume, fee percentage].
Fees Maker: A list of fee tiers for market makers.
Fee Volume Currency: ZUSD
Margin Call: 80
Margin Stop: 40
Order Minimum: 0.0001
Cost Minimum: 0.5
Tick Size: 0.1
Status: Online
Long Position Limit: 250
Short Position Limit: 200

This information provides details about the trading parameters, fees, and limits associated with the Bitcoin to US Dollar trading pair on the Kraken exchange.