from connector.dexlab import *

address = "8xhfMZpJTvuYBqzmKM3jQkzk3gcT8Pz7AnuxNUeLo6mY"

dexlab = Dexlab()
trades = dexlab.get_latest_trade_24h(address)
print(trades)