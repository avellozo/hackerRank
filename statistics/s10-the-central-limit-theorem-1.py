# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

mean = 205
n = 49
std = 15

mean2 = mean*n
std2 = std*math.sqrt(n)


def phi(x , mean, std):
    return (1 + math.erf((x-mean)/(std*math.sqrt(2))))/2


print(round(phi(9800, mean2, std2),4))
