#!/usr/bin/env python3

import threading
import time
import numpy as np
from math import *

# number of threads to use
number_of_threads = 8

# define the arrays to multiply
length = 1000 #100000000

a = np.arange(1,length)

# [1, 2, ..., length-1]

b = a[::-1]

# [length-1, length-2, ..., 1]

# define the array to store the result in
result = np.empty(a.shape)

# define the function that will multiply the threads together in parallel
def multiply(threadID, a, b):
    # we must divide the operation as evenly as possible between the threads
    #  so we define a starting and stoping index that each thread will follow

    # width will be the number of values in each array that a single thread
    #  will deal with
    width = ceil(length/number_of_threads)

    start = threadID*width
    stop = width + start

    # we do the multiplication on a subset of the arrays
    result[start:stop] = np.log(a[start:stop]*b[start:stop])

# we will record how long this takes
start = time.time()

threads=[]
for i in range(number_of_threads):
    t = threading.Thread( target = multiply, args=[i,a,b])
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.time()

multithread_duration = end-start


# now we do it in serial to compare timings
start = time.time()
result_serial = np.log(a*b)
end = time.time()

serial_duration = end-start

print("All threads finished.")
print((result==result_serial).all())
print("Multithread: ", multithread_duration,"Serial: ",serial_duration)
