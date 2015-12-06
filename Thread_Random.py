__author__ = 'Я'

import threading
import time

active = True
myNum = 0

def adder():
    global myNum
    while active:
        myNum += 1
        if myNum > 108:
            myNum = 0


def generate(count):
    global active
    threads = []
    for n in range(8):
        threads.append(threading.Thread(target=adder))
        threads[n].start()

    f = open('D:\\test', 'w')
    myStr = ''
    for n in range(count):
        time.sleep(0.0001)
        theNum = myNum % 2
        print(theNum)
        myStr += (str(theNum) + '\n')

    f.write(myStr)
    f.close()
    active = False


def make_numbers():
    f = open('D:\\test', 'r')
<<<<<<< HEAD
=======
    fu = open('D:\\numberzz', 'w')
    for i in range(32):
        newNum = 0
        for j in range(32):
            newNum *= 2
            newNum += int(f.readline())
        print(newNum)
        fu.write(str(newNum) + '\n')
>>>>>>> origin/master

    f.close()
    fu.close()


if __name__ == '__main__':
    generate(32)
    make_numbers()
