#!/usr/bin/env python3

import threading
import time

def function(i):
    print("Thread %d is active." %i)
    time.sleep(i/2)
    print("Thread %d is done." %i)

threads=[]
for i in range(1,9):
    t = threading.Thread( target = function, args=[i])
    threads.append(t)
    t.start()

print("All threads have started.")

for t in threads:
    t.join()

print("All threads finished.")
