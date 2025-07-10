import threading
import random
import time


def fun1(ev: threading.Event, n: int):
    for i in range(n):
        print("[{}] waiting for the flag to be set\n".format(i+1))
        ev.wait()
        print("Wait complete at: {}\n".format(time.ctime()))
        ev.clear()
        print()


def fun2(ev: threading.Event, n: int):
    for i in range(n):
        time.sleep(random.randrange(2, 5))
        print("Before set\n")
        ev.set()
        print("After Set\n")


ev = threading.Event()
th = []
num = random.randrange(4, 8)
th.append(threading.Thread(target=fun1, args=(ev, num)))
th[-1].start()
th.append(threading.Thread(target=fun2, args=(ev, num)))
th[-1].start()
for t in th:
    t.join()
print("All Done")
