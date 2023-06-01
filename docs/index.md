SatsDemo Document Review **index.py**

<img src="https://avatars.githubusercontent.com/u/84297388?s=200&v=4" width="200" height="200">

# Building a Flask Web App with Kraken Data

In this tutorial, we will explore how to build a web application using Flask and integrate Kraken data into it. We'll cover importing necessary modules, creating routes, and fetching ticker information from Kraken.

## Importing Modules

We begin by importing the required modules for our Flask application:

```python
from flask import Flask
from .kraken_data import getTickerInfo
```

The `Flask` module is necessary for building web applications using Flask. We also import the `getTickerInfo` function from the `kraken_data` module, which will be used to fetch ticker information from Kraken.

## Creating the Flask App

Next, we create an instance of the Flask class and assign it to the variable `app`:

```python
app = Flask(__name__)
```

Here, we use `__name__` as a special Python variable that represents the name of the current module.

## Setting Symbol Variables

We set the values of `ticker_symbol` and `long_symbol` to specific cryptocurrency symbols used for obtaining data:

```python
ticker_symbol = 'XBTUSD'
long_symbol = 'XXBTZUSD'
```

These symbols will be used when fetching ticker information from Kraken.

## Retrieving Last Closed Price

We define a function `last_close_price()` to retrieve the last closed price:

```python
def last_close_price():
    ticker = getTickerInfo(ticker_symbol)
    last_trade_closed = ticker[long_symbol]['c']
    content = "Last Trade Closed Price: " + str(last_trade_closed[0])
    return content
```

This function calls the `getTickerInfo()` function with `ticker_symbol` as an argument to retrieve ticker information from Kraken. It then extracts the last trade closed price using `long_symbol` as the key. The price is converted to a string and concatenated with a text message. The final content is returned from the function.

## Retrieving Last Ask Price

We define another function `last_ask_price()` to fetch the last ask price:

```python
def last_ask_price():
    ticker = getTickerInfo(ticker_symbol)
    last_ask = ticker[long_symbol]['a']
    content = "Last Ask Price: " + str(last_ask[0])
    return content
```

This function retrieves ticker information using the `getTickerInfo()` function. It extracts the last ask price from the data using `long_symbol` as the key. The price is converted to a string and combined with a message. The final content is returned.

## Creating Routes

We create two routes for our Flask application:

```python
@app.route('/')
def home():
    return last_ask_price()

@app.route('/about')
def about():
    return 'About'
```

The `@app.route('/')` decorator specifies that the `home()` function should be executed when the root route ("/") is accessed. The function simply returns the result of the `last_ask_price()` function.

The `@app.route('/about')` decorator indicates that the `about()` function should be executed when the "/about" route is accessed. The function returns the string "About".

## Conclusion

In this tutorial, we have explored how to build a Flask web application and integrate Kraken data into it. We have covered importing necessary modules, creating routes, and fetching ticker information from Kraken. By following this example, you can extend the application to display more data or add additional functionality as per your requirements.

**Attribution:** This content, *A Pleb Dev Contribution*, was generated with the assistance of AI using OpenAI's language model.
