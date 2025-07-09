import threading
import time
import sys
import os

startTime = time.time()
base_path = os.path.join(
    os.getcwd(), '26.ConcurrencyAndParallelism', 'problems')
lst = sys.argv
lst = lst[1:]
for file in lst:
    file_path = os.path.join(base_path, file)
    f = open(file_path, 'r')
    count = 0
    while True:
        data = f.readline()
        time.sleep(0.5)
        if data == '':
            break
        count += 1
print("File: {}, Lines: {}".format(file, count))
endTime = time.time()
print(" Time required: {}".format(endTime-startTime))
