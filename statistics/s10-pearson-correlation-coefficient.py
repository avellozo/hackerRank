import os
import sys
file = os.path.basename(__file__)
sys.stdin = open(file.split('.')[0]+"-testcases/input/input00.txt", "r")

# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as st

def Pearson(X, Y):
    m_x = st.mean(X)
    std_x = st.pstdev(X)  #the stdev method divides sum of squares by n-1
    m_y = st.mean(Y)
    std_y = st.pstdev(Y)
    n = len(X)
    ret = 0

    for i in range(n):
        ret += (X[i] - m_x)*(Y[i]-m_y)

    return (ret/(std_x*std_y*n))

n = int(input())
X = list(map(float, input().rstrip().split()))
Y = list(map(float, input().rstrip().split()))

print(round(Pearson(X,Y),3))
