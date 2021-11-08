from connector.dexlab import *

address = "8xhfMZpJTvuYBqzmKM3jQkzk3gcT8Pz7AnuxNUeLo6mY"

dexlab = Dexlab()
mp = dexlab.get_market_price(address)
print(mp)
