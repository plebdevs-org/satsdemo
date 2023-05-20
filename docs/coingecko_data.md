<img src="https://plebdevs-org.github.io/images/plebdevs.jpg" alt="PlebDevs" width="200" height="200">


# Coding Coin Gecko API Public Data: 

##A Pleb Dev 101 Task 

The Coin Gecko API is a powerful tool for accessing bitcoin market data. In this article, we will explore how to utilize the Coin Gecko API to retrieve public data such as current prices and historical prices for Bitcoin (BTC) in various currencies. We will walk through each code snippet and explain its purpose.

## Importing Libraries

We begin by importing the necessary libraries for our code:

```python
import requests
from datetime import datetime, timedelta
```

The `requests` library allows us to send HTTP requests to the Coin Gecko API, while the `datetime` and `timedelta` modules enable us to work with dates and times.

## Constants

Next, we define some constants that we will use throughout our code:

```python
API_BASE_URL = "https://api.coingecko.com/api/v3"
BTC_USD_ID = "bitcoin"
CURRENCIES = ["usd", "hkd", "eur", "gbp"]
```

- `API_BASE_URL` represents the base URL of the Coin Gecko API.
- `BTC_USD_ID` is the ID of Bitcoin in the Coin Gecko API.
- `CURRENCIES` is a list of currencies in which we want to retrieve Bitcoin prices.

## Checking API Server Status

Before making any API calls, it's a good practice to check the status of the server. We define a function `check_server_status()` to do this:

```python
def check_server_status():
    url = "https://api.coingecko.com/api/v3/ping"
    response = requests.get(url)
    if response.status_code == 200:
        return "API server is up and running."
    else:
        return "API server is not reachable."
```

This function sends a GET request to the `/ping` endpoint of the Coin Gecko API and checks the response status code. If the status code is 200, it means the server is up and running. Otherwise, it indicates that the server is not reachable.

We can now call this function to check the server status:

```python
status = check_server_status()
print(status)
```

## Retrieving Current Price

To retrieve the current price of Bitcoin in different currencies, we define the `get_price()` function:

```python
def get_price(symbol):
    url = f"{API_BASE_URL}/simple/price?ids={symbol}&vs_currencies={','.join(CURRENCIES)}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {currency: data[symbol.lower()].get(currency) for currency in CURRENCIES}
    return {}
```

This function takes a `symbol` parameter (in this case, the Bitcoin symbol) and constructs the API URL to fetch the current price. The response from the API is then parsed into a JSON object. If the status code is 200, the function returns a dictionary with the current prices of Bitcoin in the specified currencies.

Let's use this function to retrieve the current Bitcoin prices:

```python
bitcoin_prices = get_price(BTC_USD_ID)
if bitcoin_prices:
    usd_price = bitcoin_prices.get("usd")
    print(f"Bitcoin Price (USD): ${usd_price}\n")

    # Print Bitcoin prices in different currencies
    print("Bitcoin Prices in other currencies:")
    currency_symbols = {"usd": "$", "hkd": "$", "eur": "€", "gbp": "£"}
    for currency in ["hkd", "eur", "gbp"]:
        if currency != "usd":
            price = bitcoin_prices.get(currency)
            symbol = currency_symbols.get(currency)
            print(f"{currency.upper

()}: {symbol}{price}")
    print()
```

This code snippet retrieves the Bitcoin prices in USD, HKD, EUR, and GBP. It prints the USD price and then iterates over the other currencies to print their respective prices.

## Retrieving Historical Price

We can also retrieve the historical price of Bitcoin on a specific date. We define the `get_historical_price()` function for this purpose:

```python
def get_historical_price(symbol, date):
    start_date = datetime.strptime(date, "%Y-%m-%d")
    end_date = start_date + timedelta(days=1)
    start_unix_timestamp = int(start_date.timestamp())
    end_unix_timestamp = int(end_date.timestamp())

    url = f"{API_BASE_URL}/coins/{symbol}/market_chart/range?vs_currency=usd&from={start_unix_timestamp}&to={end_unix_timestamp}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        prices = data.get("prices")
        if prices:
            return prices[0][1]
    return None
```

The `get_historical_price()` function takes `symbol` (Bitcoin symbol) and `date` as parameters. It converts the `date` string into a `datetime` object and calculates the start and end dates for the API request. The function constructs the API URL using the start and end timestamps and retrieves the response.

If the status code is 200, the function extracts the historical prices from the response and returns the price at index 0. Otherwise, it returns `None`.

Let's use this function to retrieve the historical price of Bitcoin:

```python
# Get historical date (one year back from current date)
historical_date = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")

# Get Bitcoin price on the historical date
historical_price = get_historical_price(BTC_USD_ID, historical_date)
if historical_price is not None:
    formatted_historical_price = "{:.0f}".format(historical_price)
    print(f"\nHistorical Price of BTC/USD on {historical_date}: ${formatted_historical_price}")
else:
    print(f"\nUnable to retrieve historical price for BTC/USD on {historical_date}")
```

In this code snippet, we first calculate the historical date, which is one year back from the current date. We then call the `get_historical_price()` function with the Bitcoin symbol and historical date. If the historical price is successfully retrieved, it is formatted and printed. Otherwise, an error message is displayed.

## Conclusion

In this article, we have explored the positive experience of coding the Coin Gecko API to retrieve public data. We have covered how to check the server status, retrieve the current price of Bitcoin in different currencies, and fetch the historical price of Bitcoin on a specific date. By leveraging the Coin Gecko API, you can unlock a wealth of public market data for your applications and projects.





