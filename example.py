import alpaca_trade_api as tradeapi
import time

key = "PK0TI726F4O4DMX4549D"
sec = "0L9QXgvFiquroux5JlChFDoTuGppaCxivkINd3nk"

#API endpoint URL
url = "https://paper-api.alpaca.markets"

#api_version v2 refers to the version that we'll use
#very important for the documentation
api = tradeapi.REST(key, sec, url, api_version='v2')

#Init our account var
account = api.get_account()

#Should print `ACTIVE`
print(account.status)
