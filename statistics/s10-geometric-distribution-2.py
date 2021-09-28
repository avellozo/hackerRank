# Enter your code here. Read input from STDIN. Print output to STDOUT
ret = 0
for i in range(0, 5):
    ret += ((2 / 3) ** i) * (1 / 3)

print(round(ret, 3))
