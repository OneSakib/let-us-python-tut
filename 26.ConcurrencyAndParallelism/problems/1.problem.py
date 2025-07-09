import threading
import time


def fun1():
    t = threading.current_thread()
    print("Stating: ", t.name)
    time.sleep(1)
    print("Exiting", t.name)


def fun2():
    t = threading.current_thread()
    print("Stating: ", t.name)
    time.sleep(1)
    print("Exiting", t.name)


def fun3():
    t = threading.current_thread()
    print("Stating: ", t.name)
    time.sleep(1)
    print("Exiting", t.name)


t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2, name="Second Thread")
t3 = threading.Thread(target=fun3, name="Third Thread")

t1.start()
t2.start()
t3.start()
