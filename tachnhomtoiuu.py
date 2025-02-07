import math
n,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
a.sort()
count=1
for i in range(len(a)-1):
    if math.fabs(a[i]-a[i+1])>k:
        count+=1
print(count)