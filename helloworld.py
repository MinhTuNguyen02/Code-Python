import math

def isPrime(n):
    if n<2:
        return False
    for i in  range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

t=int(input())
for i in range(0,t):
    n=input()
    # ---------------
    # tmp1 = int(n)
    # tmp2 = int(n[::-1])
    # if isPrime(tmp1) and isPrime(tmp2):
    #     print("YES")
    # else:
    #     print("NO")
    # ------------------
    flag1=True; flag2=True
    for j in range(0,n.__len__()):
        if isPrime(j) and not isPrime(int(n[j])):
            flag1=False
        if not isPrime(j) and isPrime(int(n[j])):
            flag2=False
    if flag1 and flag2:
        print("YES")
    else:
        print("NO")