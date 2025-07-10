import threading


def fact(n):
    lck.acquire()
    p = 0
    if n != 0:
        t = threading.current_thread()
        p = n*fact(n-1)
        print("Thea: {}".format(t.name))
    else:
        p = 1
    lck.release()
    return p


lck = threading.RLock()
th = threading.Thread(target=fact, args=(4,))
th.start()
th2 = threading.Thread(target=fact, args=(6,))
th2.start()
th.join()
th2.join()
