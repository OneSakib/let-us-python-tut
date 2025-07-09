import threading
import time
from typing import List


def squares(nos: List, lck: threading.Lock):
    lck.acquire()
    print("Calculating Square")
    for n in nos:
        time.sleep(0.5)
        print("n={}, square={}".format(n, n*n))
    lck.release()


def cubes(nos: List, lck: threading.Lock):
    lck.acquire()
    print("Calculatin Cubes")
    for n in nos:
        time.sleep(0.5)
        print("n={}, Cube={}".format(n, n*n*n))
    lck.release()


arr = [1, 3, 5, 7, 9, 11]
startTime = time.time()
lck = threading.Lock()


th1 = threading.Thread(target=squares, args=(arr, lck))
th2 = threading.Thread(target=cubes, args=(arr, lck))
th1.start()
th2.start()
th1.join()
th2.join()
endTime = time.time()
print("Time Required : {}".format(endTime-startTime))
