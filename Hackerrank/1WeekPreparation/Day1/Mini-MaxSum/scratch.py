#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

arr = [1, 3, 5, 7, 9]

def miniMaxSum(arr):
    # Write your code here
    minSum = sum(arr) - max(arr)
    maxSum = sum(arr) - min(arr)

    print (minSum, maxSum)

miniMaxSum(arr)