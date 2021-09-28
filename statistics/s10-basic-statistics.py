import os
import sys
file = os.path.basename(__file__)
sys.stdin = open(file.split('.')[0]+"-testcases/input/input00.txt", "r")

from statistics import mean, median, multimode

n = int(input())
v = list(map(int, input().rstrip().split()))

print(round(mean(v),1))
print(round(median(v),1))
print(round(min(multimode(v)),1))
