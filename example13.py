#!/usr/bin/env python3

import multiprocessing
import threading
import numpy as np
import time

number_of_threads   = 8
number_of_processes = 8

N = 200
M = 100

matrices = [np.random.random((N,N)) for _ in range(M)]

def function(x):
    for i,row in enumerate(x):
        for j,val in enumerate(row):
            val*val*i*j

def threading_function(threadID):
    for matrix_i in np.arange(threadID, len(matrices), number_of_threads):
        matrix = matrices[matrix_i]
        for i,row in enumerate(matrix):
            for j,val in enumerate(row):
                val*val*i*j

#### Serial ####

start = time.time()

for matrix in matrices:
    function(matrix)

serial_duration = time.time()-start

#### Multithreading ####

start = time.time()

threads = []
for i in range(number_of_threads):
    t = threading.Thread(target = threading_function, args=[i])
    threads.append(t)
    t.start()

for t in threads:
    t.join()

threading_duration = time.time()-start

##################

#### Multiprocessing ####

start = time.time()

pool = multiprocessing.Pool(processes=number_of_processes)
pool.map(function,matrices)

multiprocessing_duration = time.time()-start

#################

print("Serial:          %f seconds" %(serial_duration))
print("Multithreading:  %f seconds" %(threading_duration))
print("Multiprocessing: %f seconds" %(multiprocessing_duration))
