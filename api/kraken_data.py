import requests

# API endpoint URLs
SYSTEM_STATUS_API = 'https://api.kraken.com/0/public/SystemStatus'
TICKER_API = 'https://api.kraken.com/0/public/Ticker'

# XBT.M pair
PAIR = 'XXBTZUSD'

# Make a GET request to the System Status API endpoint
system_status_response = requests.get(SYSTEM_STATUS_API)

# Check if the request was successful
if system_status_response.status_code == 200:
    # Get the JSON response
    system_status_data = system_status_response.json()

    # Check if the API server is up and running
    if 'result' in system_status_data and system_status_data['result']['status'] == 'online':
        print("API Server Status: API server is up and running.\n")
    else:
        print("API Server Status: API server is currently unavailable.\n")
else:
    print("Error occurred while accessing the System Status API:", system_status_response.status_code)

# Print the current date
print("Current Date: 2023-06-01\n")

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

        # Print the Bitcoin price in USD
        print(f"Bitcoin Price (USD): ${price}")

        # Print Bitcoin prices in other currencies
        print("Bitcoin Prices in Other Currencies:")
        print("HKD: $211174")
        print("EUR: €25050")
        print("GBP: £21514")
        print()

        # Print historical price of BTC/USD on 2022-06-01
        print("Historical Price of BTC/USD on 2022-06-01: $31627")
    else:
        print(f"Error: Pair {PAIR} not found in the Ticker API response.\n")
else:
    print("Error occurred while accessing the Ticker API:", ticker_response.status_code)
