from connector.dexlab import *
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

dexlab = Dexlab()

pairs = dexlab.get_pairs()

print(len(pairs))
addresses = pairs.address

price = dexlab.get_market_price(addresses[50])

print(price)

# orderbooks = {}
# for addr in addresses[:10]:
#     book = dexlab.get_orderbook(addr)
#     if book is not None:
#         print(book)
#         orderbooks[addr] = book


