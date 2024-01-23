#!/bin/python3

import math
import os
import random
import re
import sys

s = "12:01:00PM"

def timeConversion(s):
    # Write your code here
    if s[-2:] == "AM":
        if s[:2] == "12":
            convertedTime = "00" + s[2:-2]
        else:
            convertedTime = s[:-2]
    elif s[-2:] == "PM":
        if s[:2] == "12":
            convertedTime = s[:-2]
        else:
            convertedTime = str(int(s[:2])+12) + s[2:-2]

    print (convertedTime)


s = "07:05:45PM"
s1 = "01:33:00AM"
s2 = "12:01:00AM"
s3 = "01:33:00PM"

timeConversion(s)
timeConversion(s1)
timeConversion(s2)
timeConversion(s3)


