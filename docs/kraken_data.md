<img src="https://plebdevs-org.github.io/images/plebdevs.jpg" alt="PlebDevs" width="200" height="200">



# Integrating Kraken Data into Your Python Application: A Pleb Dev 101 Task

In this code snippet, we'll explore how to integrate Kraken data into your Python application using the Kraken API. We'll cover retrieving server time, system status, asset pairs information, ticker information, OHLC data, order book data, recent trade data, and recent spread data.

## Importing Required Modules

First, we import the necessary modules for making HTTP requests and working with JSON data:

```python
import requests
import json
```

The `requests` module allows us to send HTTP requests, while the `json` module provides functions for working with JSON data.

## Setting Up the Base URL

We set the base URL for the Kraken API:

```python
base_url = 'https://api.kraken.com/0/public'
```

The base URL will be used as the starting point for all the API endpoints.

## Retrieving Server Time

The `getServerTime()` function retrieves the server time from the Kraken API:

```python
def getServerTime():
    resp = requests.get(base_url + '/Time')
    data = resp.json()
    readable_date = data['result']['rfc1123']
    return readable_date
```

This function sends a GET request to the `/Time` endpoint and extracts the server time from the response data. The server time is returned as a readable date string.

## Retrieving System Status

The `getSystemStatus()` function retrieves the system status from the Kraken API:

```python
def getSystemStatus():
    resp = requests.get(base_url + '/SystemStatus')
    data = resp.json()
    return data['result']
```

This function sends a GET request to the `/SystemStatus` endpoint and returns the system status data from the response.

## Retrieving Asset Pairs Information

The `getAssetPairs(asset)` function retrieves asset pairs information from the Kraken API based on the specified asset:

```python
def getAssetPairs(asset):
    resp = requests.get(base_url + f'/AssetPairs?pair={asset}')
    data = resp.json()
    return data['result'][asset]
```

This function sends a GET request to the `/AssetPairs` endpoint with the specified asset as a query parameter. It returns the asset pairs information for the specified asset from the response.

## Retrieving Ticker Information

The `getTickerInfo(pair)` function retrieves ticker information from the Kraken API based on the specified pair:

```python
def getTickerInfo(pair):
    resp = requests.get(base_url + f'/Ticker?pair={pair}')
    data = resp.json()
    return data['result']
```

This function sends a GET request to the `/Ticker` endpoint with the specified pair as a query parameter. It returns the ticker information for the specified pair from the response.

## Retrieving OHLC Data

The `getOHLCdata()` function retrieves OHLC (Open, High, Low, Close) data from the Kraken API:

```python
def getOHLCdata():
    resp = requests.get(base_url + '/OHLC?pair=XBTUSD')
    data = resp.json()
    return data['result']
```

This function sends a GET request to the `/OHLC` endpoint with the default pair "XBTUSD". It returns the OHLC data from the response.

## Retrieving Order Book Data

The `getOrderBook()` function retrieves order book data from the Kraken API:

```python
def getOrderBook():
    resp = requests.get(base_url + '/Depth?pair=XBTUSD')
    data = resp.json()
   

 return data['result']
```

This function sends a GET request to the `/Depth` endpoint with the default pair "XBTUSD". It returns the order book data from the response.

## Retrieving Recent Trade Data

The `getRecentTrades()` function retrieves recent trade data from the Kraken API:

```python
def getRecentTrades():
    resp = requests.get(base_url + '/Trades?pair=XBTUSD')
    data = resp.json()
    return data['result']
```

This function sends a GET request to the `/Trades` endpoint with the default pair "XBTUSD". It returns the recent trade data from the response.

## Retrieving Recent Spread Data

The `getRecentSpreads()` function retrieves recent spread data from the Kraken API:

```python
def getRecentSpreads():
    resp = requests.get(base_url + '/Spread?pair=XBTUSD')
    data = resp.json()
    return data['result']
```

This function sends a GET request to the `/Spread` endpoint with the default pair "XBTUSD". It returns the recent spread data from the response.

## Usage Example

Here's an example of how to use the functions and print the retrieved data:

```python
if __name__ == "__main__":
    print(getServerTime())

info = getAssetPairs('XXBTZUSD')
print(info)

ticker = getTickerInfo('XBTUSD')
last_trade_closed = ticker['XXBTZUSD']['c']
print("Last Trade Closed Price: " + str(last_trade_closed[0]))

system_status = getSystemStatus()
print("System Status:", system_status)

ask_price = ticker['XXBTZUSD']['a']
print("Ask Price: " + str(ask_price[0]))

bid_price = ticker['XXBTZUSD']['b']
print("Bid Price: " + str(bid_price[0]))

info = getOHLCdata()
print(info)

info = getOrderBook()
print(info)

info = getRecentTrades()
print(info)
```

In this usage example, we first print the server time using the `getServerTime()` function. Then, we retrieve asset pairs information for 'XXBTZUSD' and print it. Next, we retrieve ticker information for 'XBTUSD' and print the last trade closed price, system status, ask price, and bid price. After that, we retrieve and print OHLC data, order book data, and recent trade data.

##Conclusion

In this code snippet, we have demonstrated how to integrate Kraken data into your Python application using the Kraken API. We covered various functionalities such as retrieving server time, system status, asset pairs information, ticker information, OHLC data, order book data, recent trade data, and recent spread data.

By leveraging the `requests` module, we sent HTTP requests to the Kraken API endpoints and obtained the desired data. The `json` module allowed us to parse the JSON response and extract the required information.

Using the provided functions, you can fetch real-time data from the Kraken exchange and incorporate it into your own projects. This can be particularly useful for building trading bots, analyzing market trends, or creating informative dashboards.

Remember to refer to the official Kraken API documentation for more details on the available endpoints, parameters, and data formats.

Feel free to customize and expand upon this code snippet based on your specific requirements and use cases.
