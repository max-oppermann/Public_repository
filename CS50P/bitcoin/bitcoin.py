'''
gotta import requests and sys
n bitcoins, sys.exit if not a float or no input (+ error message)

requests.get(https://api.coindesk.com/v1/bpi/currentprice.json)

Can format USD to 4 decimals with a thousands separator: print(f"${amount:,.4f}")
Be sure to catch any exceptions, as with code like:
try:
    ...
except requests.RequestException:
(RequestException apparently gets all of them?)

'''

import json
import requests
import sys

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    b = response.json()
    usd_rate = b["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit()

try:
    n = float(sys.argv[1])
except:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument ")
    else:
        sys.exit("Command-line argument is not a number")

cost = n*usd_rate
print(f"${cost:,.4f}")



