import os
import sys
file = os.path.basename(__file__)
sys.stdin = open(file.split('.')[0]+"-testcases/input/input00.txt", "r")


def dif(i, sub_size):
    return abs(sub_size[0] - 2 * sub_size[i])

def mostBalancedPartition(parent, files_size):
    # Write your code here
    n = len(parent)
    sub_size = [0] * n
    for i in reversed(range(n)):
        sub_size[i] += files_size[i]
        if i != 0:
            sub_size[parent[i]] += sub_size[i]

    min_dif = dif(1, sub_size)
    for i in range(2, n):
        dif_i = dif(i, sub_size)
        min_dif = min(min_dif, dif_i)
    return min_dif


if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    parent_count = int(input().strip())

    parent = []

    for _ in range(parent_count):
        parent_item = int(input().strip())
        parent.append(parent_item)

    files_size_count = int(input().strip())

    files_size = []

    for _ in range(files_size_count):
        files_size_item = int(input().strip())
        files_size.append(files_size_item)

    result = mostBalancedPartition(parent, files_size)

    fptr.write(str(result) + '\n')

    fptr.close()
