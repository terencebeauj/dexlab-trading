from connector.dexlab import *

address = "8xhfMZpJTvuYBqzmKM3jQkzk3gcT8Pz7AnuxNUeLo6mY"

dexlab = Dexlab()
market_prices = dexlab.get_market_prices()
print(market_prices)