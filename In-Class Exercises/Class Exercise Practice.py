
import math
import random

plist=[random.randint(1,25) for x in range(20)]
print plist
for x in range(20):
    print plist.index(plist[x])
for x in range(20):
    if plist.index(plist[x])%2<>0 and math.sqrt(plist[x])==int(math.sqrt(plist[x])):
        print plist[x],plist.index(plist[x])
