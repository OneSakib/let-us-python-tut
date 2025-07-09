import threading
import time


def print_numbers():
    for i in range(5):
        print("Number: {}".format(i))
        time.sleep(1)


def print_letters():
    for letter in 'ABCDE':
        print("Letter: {}".format(letter))
        time.sleep(1)


startTime = time.time()
th1 = threading.Thread(target=print_numbers)
th2 = threading.Thread(target=print_letters)
th1.start()
th2.start()
th1.join()
th2.join()
endTime = time.time()

print("Multithrading DOne....")
print("Total Time: {}".format(endTime-startTime))
