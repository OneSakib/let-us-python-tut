import threading
import time


def squares(nos):
    print("Calculating squares:\n")
    for n in nos:
        time.sleep(0.5)
        print('n= {}, squares {} \n'.format(n, n*n))


def cubes(nos):
    print("Calculating Cubes:\n")
    for n in nos:
        time.sleep(0.5)
        print("Cube {} , {} \n".format(n, n*n*n))


arr = [1, 3, 5, 7, 9, 11]
startTime = time.time()
th1 = threading.Thread(target=squares, args=(arr,))
th2 = threading.Thread(target=cubes, args=(arr,))
th1.start()
th2.start()
th1.join()  # here join is used to wait the thread while not done.
th2.join()  # here join is used to wait the thread while not done.
endTime = time.time()

print(" Time Required {} - To - {} , Total second : {}".format(startTime,
      endTime, endTime-startTime))


# It is fasrt because here one thteading calculatin and other thread value print the value
# so theare art two thread are used here.
