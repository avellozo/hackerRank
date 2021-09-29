import os
import sys
file = os.path.basename(__file__)
sys.stdin = open(file.split('.')[0]+"-testcases/input/input00.txt", "r")

#sys.stdout = open(file.split('.')[0]+"-testcases/output/output00.txt", "w")

import os


def dPos(char, board):
    p = [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == char]
    return p


def dif(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def nextMove(rinit, cinit, rd, cd):
    if rinit < rd:
        ret = 'DOWN'
    elif cinit < cd:
        ret = 'RIGHT'
    elif cinit > cd:
        ret = 'LEFT'
    else:
        ret = 'UP'
    return ret


filename = 'ps'


def readfile():
    board = []
    if os.path.exists(filename):
        with open(filename) as file:
            lines = file.readlines()
            for i in range(len(lines)):
                line = []
                for j in range(len(lines[i]) - 1):
                    line.append(lines[i][j])
                board.append(line)
    return board


def writefile(board):
    with open(filename, "w+") as file:
        for r in board:
            line = ''
            for j in r:
                line += j
            file.write(line + '\n')


def overwrite(b1, b2):
    for i in range(len(b2)):
        for j in range(len(b2[i])):
            if b1[i][j] == 'o':
                b1[i][j] = b2[i][j]


def next_move(posr, posc, board):
    # try:
    b2 = readfile()
    overwrite(board, b2)
    if board[posr][posc] == 'd':
        board[posr][posc] = '-'
        print('CLEAN')
    else:
        mind = 0
        minpos = None
        wrote = False
        init = (posr, posc)
        p = dPos('d', board)
        p = set(p)
        p.update(dPos('o', board))
        if len(p) == 0:
            p = dPos('o', board)
        for e in p:
            d = dif(init, e)
            if d < mind or mind == 0:
                mind = d
                minpos = e
            elif d == mind:
                corners = [(0, 0), (0, 4), (4, 0), (4, 4)]
                if min(dif(minpos, c) for c in corners) > min(dif(e, c) for c in corners):
                    minpos = e
        if minpos != None:
            move = nextMove(init[0], init[1], minpos[0], minpos[1])
            print(move)
    writefile(board)


# except:
#    print(b2)
#    print(board)


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)