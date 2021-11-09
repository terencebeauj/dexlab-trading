from connector.dexlab import *
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

pd.set_option("display.width", None)

dexlab = Dexlab()

while True:
    market_prices = dexlab.get_market_prices()
    df = pd.DataFrame(market_prices)
    print(df.head())