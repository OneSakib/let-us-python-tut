import threading


def print_num(n):
    rick.acquire()
    if n != 0:
        t = threading.current_thread()
        print("name : {}".format(t.name))
        n -= 1
        print_num(n)
    rick.release()


rick = threading.RLock()
th = threading.Thread(target=print_num, args=(8,))
th.start()
th2 = threading.Thread(target=print_num, args=(5,))
th2.start()
th.join()
th2.join()
