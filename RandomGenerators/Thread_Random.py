__author__ = 'Я'

import threading
import time

myNum = 0


def adder():
    global myNum
    while True:
        myNum += 1
        if myNum > 108:
            myNum = 0


for n in range(8):
    threading.Thread(target=adder).start()

f = open('D:\\test', 'w')

for n in range(1024):
    time.sleep(0.01)
    theNum = myNum % 2
    print(theNum)
    f.write(str(theNum) + '\n')

f.close()