#!/usr/bin/env python3

import time

def function(i):
    print("Thread %d is active." %i)
    time.sleep(2)
    print("Thread %d is done." %i)

function(1)
function(2)
function(3)
function(4)

print("All threads finished.")
