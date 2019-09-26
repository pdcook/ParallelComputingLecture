#!/usr/bin/env python3

from math import *
import random

runs = 10000000
total_additions = 0

current_sum = 0
for _ in range(runs):
    while current_sum <1:
        current_sum+=random.random()
        total_additions += 1
    current_sum = 0

e_approx = total_additions/runs
print("Approximate e: %f" %e_approx)
print("Exact e: %f" %e)
print("Percent error: %f%%" %((e_approx-e)*100/e))

