import math

def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True

m = int(input())
count=0
i=0
while m!=0:
    if isPrime(i):
        print(i)
        count += 1
    i += 1
    if count == m:
        break
    
    
    