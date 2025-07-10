import threading
import random
import time
import queue


def producer():
    print("Producer")
    for i in range(5):
        time.sleep(random.randrange(2, 5))
        cond.acquire()
        print("Produer Acquired")
        num = random.randrange(10, 20)
        print("Generated number : {}".format(num))
        q.append(num)
        cond.notify()
        print("Notify")
        cond.release()
        print("Producer Release")


def consumer():
    print("Consumer")
    for i in range(5):
        print("Consumer Acquired")
        cond.acquire()
        print(q)
        while True:
            if len(q):
                num = q.pop()
                break
            print("While Loop Run")
            cond.wait()
        print("It square : {}".format(num*num))
        cond.release()
        print("Consumer Release")


cond = threading.Condition()
q = []

th1 = threading.Thread(target=producer)
th2 = threading.Thread(target=consumer)
th1.start()
th2.start()
th1.join()
th2.join()
print("All Done")
