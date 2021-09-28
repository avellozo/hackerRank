# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

mean = 70
std = 10

def phi(x , mean, std):
    return (1 + math.erf((x-mean)/(std*math.sqrt(2))))/2

print(round((1-phi(80, mean, std))*100,2))
print(round((1-phi(60, mean, std))*100,2))
print(round(phi(60, mean, std)*100,2))
