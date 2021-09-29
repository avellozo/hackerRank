import os
import sys
file = os.path.basename(__file__)
sys.stdin = open(file.split('.')[0]+"-testcases/input/input00.txt", "r")

def displayPathtoPrincess(n,grid):
#print all the moves here
    mid = int(n/2)
    if grid[0][0] == 'p':
        for _ in range(mid):
            print('LEFT')
            print('UP')
    elif grid[0][n-1] == 'p':
        for _ in range(mid):
            print('RIGHT')
            print('UP')
    elif grid[n-1][0] == 'p':
        for _ in range(mid):
            print('LEFT')
            print('DOWN')
    elif grid[n-1][n-1] == 'p':
        for _ in range(mid):
            print('RIGHT')
            print('DOWN')


m = int(input())
grid = []
for _ in range(m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)