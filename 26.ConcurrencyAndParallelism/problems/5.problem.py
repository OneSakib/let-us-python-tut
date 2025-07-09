import threading
import time
import sys
import os

startTime = time.time()
base_path = os.path.join(
    os.getcwd(), '26.ConcurrencyAndParallelism', 'problems')
lst = sys.argv
lst = lst[1:]


def readFile(inputFile):
    file_path = os.path.join(base_path, inputFile)
    f = open(file_path, 'r')
    count = 0
    while True:
        data = f.readline()
        time.sleep(0.5)
        if data == '':
            break
        count += 1
    print("File: {}, Lines: {}".format(inputFile, count))


threads = []
for file in lst:
    th = threading.Thread(target=readFile, args=(file,))
    th.start()
    threads.append(th)


for th in threads:
    th.join()

endTime = time.time()
print(" Time required: {}".format(endTime-startTime))
