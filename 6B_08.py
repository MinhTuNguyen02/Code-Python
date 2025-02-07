n = int(input())
bang=[]
for i in range(0,n):
    ten = input("Nhap ten:")
    tl = input("Nhap the loai:")
    sl = input("Nhap so luong:")
    gia = input("Nhap gia tien:")
    nph = input("Nhap ngay phat hanh:")
    tmp = (ten,tl,sl,gia,nph) 
    bang.append(tmp)

min = 999999
tpl=()
print("ds:")
for i in bang:
    if int(i[3]) < min:
        min = int(i[3])
        tpl=i
    for j in range(len(i)):
        print(i[j],end=" ")
    print("")

print("gia re nhat:")
print(tpl[0],tpl[1],tpl[3],end=" ")