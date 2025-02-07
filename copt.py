def check(n):
    s=str(n)
    res = 1
    for i in s: 
        res += int(i)
    return res

def aaa():
    q=int(input())
    a = [int(i) for i in input().split()]
    for i in range(0,q-1):
        for j in range(i+1,q):
            if(check(a[j])<check(a[i]) or (check(a[j])==check(a[i]) and a[j]<a[i])):
                a[j], a[i] = a[i], a[j]
    print(*a,sep=" ")
    print()


for i in range(int(input())): aaa()
