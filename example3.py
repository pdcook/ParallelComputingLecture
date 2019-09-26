#!/usr/bin/env python3

import threading
import time

def function(i):
    print("Thread %d is active." %i)
    time.sleep(i/2)
    print("Thread %d is done." %i)

for i in range(1,9):
    t = threading.Thread( target = function, args=[i])
    t.start()


print("All threads finished.")
