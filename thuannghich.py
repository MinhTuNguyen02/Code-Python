t=int(input())
for i in range(0,t):
    n=input()
    tong=0
    for j in range(0,n.__len__()):
        tong += int(n[j])
    if tong==int(str(tong)[::-1]) and tong>=10:
        print("YES")
    else:
        print("NO")
    