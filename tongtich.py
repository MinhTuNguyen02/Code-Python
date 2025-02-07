t=int(input())
for i in range(0,t):
    n=input()
    tong=0
    tich=1
    flag=True
    for j in range(0,n.__len__()):
        if j%2==0:
            tong += int(n[j])
        elif n[j]!="0":
            flag=False
            tich *= int(n[j])
    if flag:
        tich=0
    print(tong,tich)