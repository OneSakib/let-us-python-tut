import time
import threading


def fun1():
    print("Entering 1")
    global g
    g += 1
    time.sleep(0.5)
    g -= 1
    print("in Fun 1 g= {}".format(g))
    print("Exit fun1")


def fun2():
    print("Entering 2")
    global g
    g += 1    
    g -= 1
    print("in Fun 2 g= {}".format(g))
    print("Exit fun2")


g = 10

th1 = threading.Thread(target=fun1)
th2 = threading.Thread(target=fun2)
th1.start()
th2.start()
th1.join()
th2.join()
