#!/bin/python3

import math
import random
import re
import sys
import statistics as s
import os
import sys
file = os.path.basename(__file__)
sys.stdin = open(file.split('.')[0]+"-testcases/input/input00.txt", "r")

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
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

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
