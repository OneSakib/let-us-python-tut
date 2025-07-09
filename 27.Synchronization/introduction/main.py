import threading
# lck = threading.Lock()
# lck.acquire()
# lck.release()
import time


def fun1():
    print("Function 1 is Running")
    count = 0
    while count < 10:
        print("Function 1 : {}".format(count), end="\n")
        ev.wait()
        print("Function 1 is Cleared \n", end="\n")
        ev.clear()
        count += 1


def fun2():
    print("Function 2 is Running")
    count = 0
    while count < 10:
        print("Function 2 : {}".format(count), end="\n")
        time.sleep(1)
        ev.set()
        print("Function 2 is Cleared", end="\n")
        count += 1


ev = threading.Event()
th1 = threading.Thread(target=fun1)
th2 = threading.Thread(target=fun2)
th1.start()
th2.start()
