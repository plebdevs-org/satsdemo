import requests
from datetime import datetime, timedelta

# Constants
API_BASE_URL = "https://api.coingecko.com/api/v3"
BTC_USD_ID = "bitcoin"
CURRENCIES = ["usd", "hkd", "eur", "gbp"]

def check_server_status():
    url = "https://api.coingecko.com/api/v3/ping"
    response = requests.get(url)
    if response.status_code == 200:
        return "API server is up and running."
    else:
        return "API server is not reachable."

def get_price(symbol):
    url = f"{API_BASE_URL}/simple/price?ids={symbol}&vs_currencies={','.join(CURRENCIES)}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {currency: data[symbol.lower()].get(currency) for currency in CURRENCIES}
    return {}

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

# Check API server status
status = check_server_status()
print(status)

# Get current date
current_date = datetime.now().strftime("%Y-%m-%d")
print(f"\nCurrent Date: {current_date}\n")

# Get Bitcoin price in USD
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
            print(f"{currency.upper()}: {symbol}{price}")
    print()

# Get historical date (one year back from current date)
historical_date = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")

# Get Bitcoin price on the historical date
historical_price = get_historical_price(BTC_USD_ID, historical_date)
if historical_price is not None:
    formatted_historical_price = "{:.0f}".format(historical_price)
    print(f"\nHistorical Price of BTC/USD on {historical_date}: ${formatted_historical_price}")
else:
    print(f"\nUnable to retrieve historical price for BTC/USD on {historical_date}")
