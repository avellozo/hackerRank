# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def binom(x, n, p):
    return (nfact/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))

p = 1.09/2.09
n = 6
nfact= math.factorial(n)

ret = 0
for i in range(0,3):
    ret += binom(i, n, p)

print(round(1-ret,3))
