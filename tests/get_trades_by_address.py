from connector.dexlab import *

address = "8xhfMZpJTvuYBqzmKM3jQkzk3gcT8Pz7AnuxNUeLo6mY"

dexlab = Dexlab()
trades = dexlab.get_trades_by_address(address)
print(trades)