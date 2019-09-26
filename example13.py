#!/usr/bin/env python3

import multiprocessing
import threading
import numpy as np
import time
import copy

number_of_threads   = 8
number_of_processes = 8

N = 200
M = 100

matrices = [np.random.random((N,N)) for _ in range(M)]
matrices_2 = copy.deepcopy(matrices)
matrices_3 = copy.deepcopy(matrices)

def function(matrix):
    for i,row in enumerate(matrix):
        for j,val in enumerate(row):
            matrix[i][j] = val*val*i*j
    return matrix

def threading_function(threadID):
    for matrix_i in np.arange(threadID, len(matrices_2), number_of_threads):
        matrix = matrices_2[matrix_i]
        for i,row in enumerate(matrix):
            for j,val in enumerate(row):
                matrix[i][j] = val*val*i*j
        threading_results[matrix_i] = matrix

#### Serial ####

start = time.time()

serial_results = []

for matrix_i, matrix in enumerate(matrices):
    serial_results.append(function(matrix))

serial_duration = time.time()-start

#### Multithreading ####

start = time.time()
threading_results = ["" for _ in range(M)]

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
processing_results = pool.map(function,matrices_3)

multiprocessing_duration = time.time()-start

#################

# check to see if the results are all equal
print("Consistent: ", ((np.array(processing_results)==np.array(threading_results)).all() and (np.array(processing_results)==np.array(serial_results)).all()))

# print the amount of time taken by each
print("Serial:          %f seconds" %(serial_duration))
print("Multithreading:  %f seconds" %(threading_duration))
print("Multiprocessing: %f seconds" %(multiprocessing_duration))
