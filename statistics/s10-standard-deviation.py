#!/bin/python3

import math

import random
import re
import os
import sys
file = os.path.basename(__file__)
sys.stdin = open(file.split('.')[0]+"-testcases/input/input00.txt", "r")


#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    n = len(arr)
    mean = sum(arr)/n
    sq = 0
    for e in arr:
        sq += (e-mean)**2
    return math.sqrt(sq/n)

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    print(round(stdDev(vals),1))
