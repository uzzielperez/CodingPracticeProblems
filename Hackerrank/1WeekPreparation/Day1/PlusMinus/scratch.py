#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

arr = [1, 1, 0, -1, -1]

def plusMinus(arr):
	nPos, nNeg, nZero, nTotal = 0, 0, 0, len(arr)
	for e in arr: 
		if e > 0:
			nPos = nPos + 1 
		if e < 0:
			nNeg = nNeg + 1
		if e == 0:
			nZero = nZero + 1 

	print("nPos: %d, nNeg: %d, nZero: %d, nTotal: %d" %(nPos, nNeg, nZero, nTotal))

	# To print 6 decimal places after do f"{result:.6f}"
	print(f"{nPos/nTotal:.6f}")
	print(f"{nNeg/nTotal:.6f}")
	print(f"{nZero/nTotal:.6f}")

plusMinus(arr)