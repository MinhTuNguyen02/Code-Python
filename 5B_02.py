import math

x = int(input())
n = int(input())
s=0
for i in range (1,n+1):
    s += math.pow(x,2*i)

print(s)