n = int(input())

if n==0:
    print("không có số nào được nhập vào")
    exit()

max=-999999
for i in range(0,n):
    m=float(input("nhập số thứ {0}: ".format(i+1)))
    if m>max:
        max=m

print(max)


