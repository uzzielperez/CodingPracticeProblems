#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

a = [1, 2, 3, 4, 1, 2, 3]
def lonelyinteger(a):
    # Write your code here

    # Using a dictionary solution
    store = {}
    for e in a:
        if e in store:
            store[e] += 1 
        else:
            store[e] = 1
    
    for key, value in store.items():
        if value == 1:
            print (key)

def elonelyinteger(a):
    # Write your code here
    result = 0
    for e in a:
        result ^= e
    print(result)

    

lonelyinteger(a)
elonelyinteger(a)

    