import threading
# t = threading.current_thread()
# print(">Current Thread", t)
# print(">Current Thread", t.name)
# print(">Current Thread", t.ident)
# print(">Current Thread", t.is_alive())
# t.name = "My Thread"
# print(t.name)


# Thread creation

# def my_func():
#     print("First Thread Called")


# def my_func2():
#     print("Second Thread Called")


# th1 = threading.Thread(name="My FIrst Thread", target=my_func)
# th2 = threading.Thread(target=my_func2)

# th1.start()
# th2.start()


# Mehto 2


# class SquareGeneratorThread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)

#     def run(self):
#         print("Launching")


# th = SquareGeneratorThread()
# th.start()


# Passing Perametor
def squares(a, b):
    print(">>>Square :", a**b)


def cubes(a):
    print("Cube of {} : {}".format(a, a**3))


a = 10
b = 2
th1 = threading.Thread(target=squares, args=(a, b))
th2 = threading.Thread(target=cubes, args=(a,))

th1.start()
th2.start()
