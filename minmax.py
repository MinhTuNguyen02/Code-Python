n=int(input())
tong=0.0
diem=[]
max=-1
min=11
for i in range(0,n):
    d=float(input())
    diem.append(d)
    if d>max:
        max=d
    if d<min:
        min=d

for o in diem:
    if o==max:
        diem.remove(o)
        n-=1
    if o==min:
        diem.remove(o)
        n-=1

for j in diem:
    tong+=j
tb=round(tong/n)
print(tb)
