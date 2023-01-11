import os

totalSize = 0
for filename in os.listdir('/Users/maxmcdonough/Projects/python-test'):
    if not os.path.isfile(os.path.join('/Users/maxmcdonough/Projects/python-test', filename)):
        continue
    print(totalSize)
    totalSize = totalSize + os.path.getsize((os.path.join('/Users/maxmcdonough/Projects/python-test', filename)))

print(totalSize)


