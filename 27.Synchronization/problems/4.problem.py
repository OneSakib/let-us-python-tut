import time
import threading
# from types import List


def printMsg(msg: str, lck: threading.Lock):
    lck.acquire()
    print("[", end="")
    print(msg, end="")
    time.sleep(0.5)
    print(']', end="")
    lck.release()


lck = threading.Lock()
th1 = threading.Thread(target=printMsg, args=('What is this life....', lck))
th1.start()

th2 = threading.Thread(target=printMsg, args=('We have no time', lck))
th2.start()


th3 = threading.Thread(target=printMsg, args=('To stand and start...', lck))

th3.start()

th1.join()
th2.join()
th3.join()
