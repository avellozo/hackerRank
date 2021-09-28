import os
import sys
file = os.path.basename(__file__)
sys.stdin = open(file.split('.')[0]+"-testcases/input/input00.txt", "r")

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''import numpy as np

def rank(arr):
    array = np.array(arr)
    temp = array.argsort()
    ranks = np.empty_like(temp)
    ranks[temp] = np.arange(len(array))
    return ranks
'''

def rank(arr):
    n = len(arr)
    arr_sorted = sorted(arr)
    ranks = [0]*n
    for i in range(n):
        ranks[i] = arr_sorted.index(arr[i])
    return ranks


def Spearman(X, Y):
    n = len(X)
    rx= rank(X)
    ry = rank(Y)
    ret = 0

    for i in range(n):
        ret += (rx[i] - ry[i]) ** 2

    return 1-(6*ret / (n*(n**2-1)))


n = int(input())
X = list(map(float, input().rstrip().split()))
Y = list(map(float, input().rstrip().split()))

print(round(Spearman(X, Y), 3))
