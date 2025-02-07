s=input()
res=set()
for i in range(0,len(s)-1,2):
    res.add(int(s[i]+s[i+1]))
res=list(res)
res.sort()
print(*res,sep=' ')