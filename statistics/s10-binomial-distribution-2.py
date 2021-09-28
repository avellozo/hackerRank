# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def binom(x, n, p):
    return (nfact/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))

p = 0.12
n = 10
nfact= math.factorial(n)

ret = 0
for i in range(0,2):
    ret += binom(i, n, p)

ret2= ret
ret += binom(2, n, p)
print(round(ret,3))
print(round(1-ret2,3))
