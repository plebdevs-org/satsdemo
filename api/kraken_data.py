import requests
from datetime import date, timedelta
import pandas as pd

# Kraken API endpoint URLs and Constants
BASE_URL = "https://api.kraken.com/0/public"
SYSTEM_STATUS_API = f"{BASE_URL}/SystemStatus"
TICKER_API = f"{BASE_URL}/Ticker"
OHLC_API = f"{BASE_URL}/OHLC"  # Historical price API endpoint

# XBT.M pair
PAIR = 'XXBTZUSD'

# Function to get historical price from Kraken
def get_historical_price(pair, date):
    interval = 1  # 1-minute interval
    url = f"{OHLC_API}?pair={pair}&interval={interval}&since={date}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'result' in data and pair in data['result']:
            prices = data['result'][pair]
            if len(prices) > 0:
                price = prices[0][4]  # Closing price
                return price
    return None

def get_data():
    data = []

    # Add a print statement with an empty string to create spaces
    data.append("")

    # Make a GET request to the System Status API endpoint
    system_status_response = requests.get(SYSTEM_STATUS_API)

    # Check if the request was successful
    if system_status_response.status_code == 200:
        # Get the JSON response
        system_status_data = system_status_response.json()

        # Check if the API server is up and running
        if 'result' in system_status_data and system_status_data['result']['status'] == 'online':
            data.append("The Kraken API server is up and running.\n")
        else:
            data.append("The Kraken API server is currently unavailable.\n")
    else:
        data.append("Error occurred while accessing the System Status API:", system_status_response.status_code)

    # Print the current date
    current_date = date.today().strftime("%Y-%m-%d")
    data.append(f"Current Date: {current_date}\n")

    # Make a GET request to the Ticker API endpoint
    ticker_response = requests.get(f"{TICKER_API}?pair={PAIR}")

    # Check if the request was successful
    if ticker_response.status_code == 200:
        # Get the JSON response
        ticker_data = ticker_response.json()

        # Check if the result is available in the response
        if 'result' in ticker_data and PAIR in ticker_data['result']:
            # Retrieve the Bitcoin price
            price = ticker_data['result'][PAIR]['c'][0]

            # Print the Bitcoin price in USD without decimals
            data.append("Bitcoin Price (USD): ${:,.0f}".format(float(price)))

            # Add a print statement with an empty string to create spaces
            data.append("")

            # Print Bitcoin prices in other currencies without decimals
            data.append("Bitcoin Prices in Other Currencies:\n")
            data.append("HKD: ${:,.0f}".format(211174))
            data.append("EUR: €{:,.0f}".format(25050))
            data.append("GBP: £{:,.0f}".format(21514))
            data.append("")

    # Calculate historical date (365 days ago from the current date)
    current_date = date.today()  # Use date.today() instead of current_date_str
    historical_date = (current_date - timedelta(days=365)).strftime("%Y-%m-%d")

    # Get Bitcoin price on the historical date
    historical_price = get_historical_price(PAIR, historical_date)
    if historical_price is not None:
        formatted_historical_price = "{:,.0f}".format(float(historical_price))
        data.append(f"Historical Price of BTC/USD on {historical_date}: ${formatted_historical_price}\n")

        # Modify the print statement for compared HKD historical price
        formatted_historical_btcusd_rate = "30,229"  # Example value
        data.append(f"Compared to HKD Historical Price BTC/USD on {historical_date}: ${formatted_historical_btcusd_rate}")
    else:
        data.append(f"Unable to retrieve historical price for BTC/USD on {historical_date}")

    return data

if __name__ == '__main__':
    result = get_data()
    for item in result:
        print(item)
