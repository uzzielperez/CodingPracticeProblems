#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    sumLR, sumRL = 0, 0 
    i = 0 
    
    while i < n:
        sumLR += arr[i][i]
        sumRL += arr[i][n-1-i]
        i += 1
    diagDiff = abs(sumLR-sumRL)
    return diagDiff
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
        
    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()