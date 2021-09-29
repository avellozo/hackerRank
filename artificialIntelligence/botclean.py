import os
import sys
file = os.path.basename(__file__)
sys.stdin = open(file.split('.')[0]+"-testcases/input/input00.txt", "r")

#sys.stdout = open(file.split('.')[0]+"-testcases/output/output00.txt", "w")

def dPos(char,board):
    p = [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == char]
    return p

def dif(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def nextMove(rinit, cinit, rd, cd):
    if cinit < cd:
        ret = 'RIGHT'
    elif cinit > cd:
        ret = 'LEFT'
    elif rinit < rd:
        ret = 'DOWN'
    else:
        ret = 'UP'
    return ret

def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        board[posr][posc] = '-'
        print('CLEAN')
        next_move(posr, posc, board)
    else:
        mind = 0
        minpos = None
        init = (posr, posc)
        p = dPos('d', board)
        for e in p:
            d = dif(init, e)
            if d < mind or mind == 0:
                mind = d
                minpos = e
        if minpos != None:
            move = nextMove(init[0], init[1], minpos[0], minpos[1])
            print(move)
            if move == 'RIGHT':
                posc += 1
            elif move == 'LEFT':
                posc -= 1
            elif move == 'UP':
                posr -= 1
            elif move == 'DOWN':
                posr += 1
            next_move(posr, posc, board)

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    initr = pos[0]
    initc = pos[1]
    next_move(initr, initc, board)

# filename = "myfile.txt"
#
# with open( filename ) as f:
#
#     # file read can happen here
#
#     # print "file exists"
#
#     print f.readlines()
#
# with open( filename, "w") as f:
#
#     # print "file write happening here"
#
#     f.write("write something here ")