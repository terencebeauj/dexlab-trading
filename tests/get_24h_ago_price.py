from connector.dexlab import *

address = "8xhfMZpJTvuYBqzmKM3jQkzk3gcT8Pz7AnuxNUeLo6mY"

dexlab = Dexlab()
price = dexlab.get_24h_ago_price(address)
print(price)