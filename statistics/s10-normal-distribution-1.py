# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

mean = 20
std = 2

def phi(x , mean, std):
    return (1 + math.erf((x-mean)/(std*math.sqrt(2))))/2

print(round(phi(19.5, mean, std),3))
print(round(phi(22, mean, std)-phi(20, mean, std),3))
