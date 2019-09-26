#!/usr/bin/env python3

import threading
import time

def function(i):
    print("Thread %d is active." %i)
    time.sleep(2)
    print("Thread %d is done." %i)

t1 = threading.Thread( target = function, args=[1])
t2 = threading.Thread( target = function, args=[2])
t3 = threading.Thread( target = function, args=[3])
t4 = threading.Thread( target = function, args=[4])

print("No active threads.\n----------")
time.sleep(2)

print("Starting Thread 1.")
t1.start()
print("Starting Thread 2.")
t2.start()
print("Starting Thread 3.")
t3.start()
print("Starting Thread 4.")
t4.start()


t1.join()
t2.join()
t3.join()
t4.join()

print("All threads finished.")
