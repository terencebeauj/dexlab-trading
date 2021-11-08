from connector.dexlab import *

dexlab = Dexlab()

trades = dexlab.get_latests_trades()
print(trades)