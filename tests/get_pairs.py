from connector.dexlab import *
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option("display.width", None)


dexlab = Dexlab()

pairs = dexlab.get_pairs()

df = pd.DataFrame(pairs)
print(df.head())