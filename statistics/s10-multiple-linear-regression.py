import os
import sys
file = os.path.basename(__file__)
sys.stdin = open(file.split('.')[0]+"-testcases/input/input00.txt", "r")

from sklearn.linear_model import LinearRegression
import numpy as np

line = input().strip().split()
m = int(line[0])
n = int(line[1])

nxm = [0]*n
y = [0]*n
for i in range(n):
    f = list(map(float, input().strip().split()))
    y[i] = f.pop()
    nxm[i] = f

q = int(input().strip())
qxm = [0]*q
for i in range(q):
    f = list(map(float, input().strip().split()))
    qxm[i] = f

reg = LinearRegression().fit(nxm, y)
res = reg.predict(qxm)
#for e in res:
#    print(e)

for i in range(n):
    nxm[i].insert(0,1)
xt = np.array(nxm).transpose()
xi = np.linalg.inv(np.dot(xt, nxm))
b = np.dot(np.dot(xi, xt),y)
for e in qxm:
    e.insert(0,1)
    print(np.dot(e,b))

