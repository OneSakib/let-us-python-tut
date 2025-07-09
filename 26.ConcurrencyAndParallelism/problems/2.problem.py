import threading
import time


def squares(nos):
    print("Calculating squares")
    for n in nos:
        time.sleep(0.5)
        print('n= {}, squares {}'.format(n, n*n))


def cubes(nos):
    print("Calculating Cubes:")
    for n in nos:
        time.sleep(0.5)
        print("Cube {} , {} ".format(n, n*n*n))


arr = [1, 3, 5, 7, 9, 11]
startTime = time.time()
squares(arr)
cubes(arr)
endTime = time.time()

print(" Time Required {} - To - {} , Total second : {}".format(startTime,
      endTime, endTime-startTime))
