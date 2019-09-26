#!/usr/bin/env python3

import threading
import time
import numpy as np
from math import *
import random

# number of threads to use
number_of_threads = 8

runs = 1000000

#### Serial ####

start = time.time()

total_additions = 0
for _ in range(runs):
    current_sum = 0
    while current_sum <1:
        current_sum+=random.random()
        total_additions += 1

e_approx_serial = total_additions/runs

serial_duration = time.time()-start

###############

#### Parallel ####

run_results = np.empty(runs)

def MonteCarlo(threadID, run_results):
    for i in np.arange(threadID,runs,number_of_threads):
        current_sum = 0
        additions = 0
        while current_sum <1:
            current_sum += random.random()
            additions += 1
        run_results[i] = additions

# we will record how long this takes
start = time.time()

threads=[]
for i in range(number_of_threads):
    t = threading.Thread( target = MonteCarlo, args=[i, run_results])
    threads.append(t)
    t.start()

for t in threads:
    t.join()

e_approx_parallel = np.sum(run_results)/runs
parallel_duration = time.time()-start



print("Approximate e: %f (Serial: %f seconds)" %(e_approx_serial,serial_duration))
print("Approximate e: %f (Parallel: %f seconds)" %(e_approx_parallel,parallel_duration))
print("Percent difference: %f%%" %(abs(e_approx_parallel-e_approx_serial)*100/((e_approx_serial+e_approx_parallel)/2)))

