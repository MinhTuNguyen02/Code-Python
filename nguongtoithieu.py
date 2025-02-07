s=input()
k=int(input())
res=set()
a=[]
for i in range(0,len(s)-1,2):
    res.add(int(s[i]+s[i+1]))
    a.append(int(s[i]+s[i+1]))
res=list(res)
res.sort()
f=False
for i in res:
    if a.count(i)>=k:
        f=True
        print(i,a.count(i))
if not f: print("NOT FOUND")

     