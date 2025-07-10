import threading


def fun(msg):
    s.acquire()
    t = threading.current_thread()
    while True:
        print("Name: {}, Message : {}".format(t.name, msg))
    s.release()


s = threading.BoundedSemaphore(3)
th1 = threading.Thread(target=fun, args=("Hello....",))
th2 = threading.Thread(target=fun, args=("Hi....",))
th3 = threading.Thread(target=fun, args=("Welcome...",))
th4 = threading.Thread(target=fun, args=("Byyyy",))

th1.start()
th2.start()
th3.start()
th4.start()
# join
th1.join()
th2.join()
th3.join()
th4.join()
