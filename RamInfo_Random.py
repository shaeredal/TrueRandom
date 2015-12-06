import psutil
import time
import math

items = []

with open("numbers.txt", "w") as f:
    f.write('')

while len(items) != 1000:
    n = psutil.virtual_memory()[3]
    time.sleep(0.05)
    s = psutil.virtual_memory()[3]
    if n != s:
        s = math.ceil(s / 100)
        items.append(s)
        print(s)

with open("numbers.txt", "a") as f:
    for x in items:
        f.write('{}\n'.format(x % 2))
