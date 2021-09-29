import os
import sys
file = os.path.basename(__file__)
sys.stdin = open(file.split('.')[0]+"-testcases/input/input00.txt", "r")

def princessPos(n,grid):
    p = grid.find('p')
    r = p//n
    c = p%n
    return r,c

def nextMove(n,r,c,grid):
    rp, cp = princessPos(n,grid)
    if c < cp:
        ret = 'RIGHT'
    elif c > cp:
        ret = 'LEFT'
    elif r < rp:
        ret = 'DOWN'
    else:
        ret = 'UP'
    return ret

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = ""
for i in range(n):
    grid += input()

print(nextMove(n,r,c,grid))