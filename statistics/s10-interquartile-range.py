#!/bin/python3

import math
import os
import random
import re
import sys
import statistics as s
import os
import sys
file = os.path.basename(__file__)
sys.stdin = open(file.split('.')[0]+"-testcases/input/input00.txt", "r")

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def quartiles(arr):
    # Write your code here
    arr = sorted(arr)
    ret = []
    n = len(arr)
    mid = n//2
    ret.append(int(s.median(arr[:mid])))
    ret.append(int(s.median(arr)))
    if (n%2 !=0):
        ret.append(int(s.median(arr[mid+1:])))
    else:
        ret.append(int(s.median(arr[mid:])))
    return ret

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    arr = []
    for v,f in zip(values,freqs):
        a = [v]*f
        arr += a
    ret = quartiles(arr)
    return float(ret[2]-ret[0])

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    print(round(interQuartile(val, freq),1))
