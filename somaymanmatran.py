n,m=[int(i) for i in input().split()]
a=[]
ma=-1
mi=10**9
for i in range(n):
    tmp=[int(x) for x in input().split()]
    if max(tmp)>ma: ma=max(tmp)
    if min(tmp)<mi: mi=min(tmp)
    a.append(tmp)

target=ma-mi
f=False
f1=True
for i in range(0,n):
    for j in range(0,m):
        if a[i][j]==target:
            f=True
            if f and f1: 
                print(target)
                f1=False
            print("Vi tri [{}][{}]".format(i,j))
if not f:
    print("NOT FOUND")
