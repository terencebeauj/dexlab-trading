from connector.dexlab import *

dexlab = Dexlab()
volumes = dexlab.get_volumes()
print(volumes)