n,m=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]


for i in range(min(m,n)):
    if i==n or i==m: break
    if a[i] in b:
        print(a[i],end=' ')
print()
for i in a:
    if not (i in b):
        print(i,end=' ')
print()
for i in b:
    if not (i in a):
        print(i,end=' ')