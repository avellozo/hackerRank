# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

mean = 2.4
n = 100
std = 2

mean2 = mean*n
std2 = std*math.sqrt(n)

def phi(x , mean, std):
    return (1 + math.erf((x-mean)/(std*math.sqrt(2))))/2

print(round(phi(250, mean2, std2),4))
