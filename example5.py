#!/usr/bin/env python3

import threading
import time
import numpy as np

number_of_threads = 8

def function(threadID,values):
    values[threadID] = threadID**2

threads=[]
values = np.empty(number_of_threads)
for i in range(number_of_threads):
    t = threading.Thread( target = function, args=[i,values])
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads finished.")
print(values)
