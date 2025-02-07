n,m=[int(i) for i in input().split()]
a=[]
for i in range(n):
    tmp=[int(x) for x in input().split()]
    a.append(tmp)

if n>m:
    for i in range(0,n):
        if i%2==0 and n!=m:
            n-=1
            continue
        print(*a[i],sep=' ')
else:
    for i in range(0,n):
        l=m-n
        for j in range(0,m):
            if j%2!=0 and l!=0:
                l-=1
                continue
            print(a[i][j],end=" ")
        print()

    
