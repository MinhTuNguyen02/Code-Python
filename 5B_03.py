y = int(input("Nhap tien gui: "))
z = int(input("Nhap tien mong muon: "))
x = int(input("Nhap lai xuat: "))

thang=0
while True:
    y += y*x/100
    thang+=1
    if y >= z:
        break

print(thang,"thang")