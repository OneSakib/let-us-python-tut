import multiprocessing
import time


def cal_squares(numbers):
    for n in numbers:
        print(" Square of {} : {}".format(n, n*n))
        time.sleep(1)


def cal_cubes(numbers):
    for n in numbers:
        print("Cube of {} : {}".format(n, n*n*n))
        time.sleep(1)


if __name__ == '__main__':
    startTime = time.time()
    nums = [1, 2, 3, 4, 5]
    p1 = multiprocessing.Process(target=cal_squares, args=(nums,))
    p2 = multiprocessing.Process(target=cal_cubes, args=(nums,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    endTime = time.time()
    print("Multiprocsssing Done")
    print("Total Time: {}".format(endTime-startTime))
