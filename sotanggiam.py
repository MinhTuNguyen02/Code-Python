def check(n):
    a=[int(i) for i in n]
    d=max(a)
    idx=a.index(d)
    f1=True;f2=True
    for i in range(0,idx):
        if a[i]>=a[i+1]:
            f1=False
    for i in range(idx,len(a)-1):
        if a[i]<=a[i+1]:
            f2=False
    if f1 and f2: return True
    else: return False

for i in range(int(input())):
    n=input()
    if len(n)>=3 and check(n):
        print("YES")        
    else:
        print("NO")
