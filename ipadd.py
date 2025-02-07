n=int(input())
for i in range(n):
    ip=input().split('.')
    flag=True
    for j in ip:
        if int(j) > 255 or int(j)<0:
            flag=False
            break
    if flag:
        print("YES",end="\n")
    else:
        print("NO",end="")
