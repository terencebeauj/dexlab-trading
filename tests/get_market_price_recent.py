from connector.dexlab import *

dexlab = Dexlab()
recent = dexlab.get_market_price_recent()
print(recent)