#!/usr/bin/env python3

import multiprocessing # <<<
import time
import numpy as np
from math import *
import random

# number of processes to use
number_of_processes = 8

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

def MonteCarlo(processID):
    process_results = []
    for i in np.arange(processID,runs,number_of_processes):
        current_sum = 0
        additions = 0
        while current_sum <1:
            current_sum += random.random()
            additions += 1
        process_results.append(additions)
    return process_results

# we will record how long this takes
start = time.time()

pool = multiprocessing.Pool(processes=number_of_processes)
run_results = pool.map(MonteCarlo, range(number_of_processes))

e_approx_parallel = np.sum(run_results)/runs
parallel_duration = time.time()-start

print("Approximate e: %f (Serial: %f seconds)" %(e_approx_serial,serial_duration))
print("Approximate e: %f (Parallel: %f seconds)" %(e_approx_parallel,parallel_duration))
print("Percent difference: %f%%" %(abs(e_approx_parallel-e_approx_serial)*100/((e_approx_serial+e_approx_parallel)/2)))

