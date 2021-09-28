# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def poisson(k, l):
    return l**k*math.e**(-l)/(math.factorial(k))

k = 5
l = 2.5

print (round(poisson(k,l),3))
