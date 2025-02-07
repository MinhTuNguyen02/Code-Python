n=input()
n=n[::-1]
a=[]
for i in range(0,len(n),3):
    a.append(n[0+i:3+i])
res=''
for i in a:
    t=0
    for j in range(len(i)):
        if i[j]=='1':
            t+=2**j
    res=str(t)+res
print(res)