import quandl

quandl.read_key('api_key_secret')

raw = quandl.get(["GDAX/ETH_EUR", "NASDAQOMX/OMXN40"])

raw.columns

raw.info()

help(quandl.get)
