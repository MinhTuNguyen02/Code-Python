while True:
    h = int(input("Nhap gio:"))
    m = int(input("Nhap phut:"))
    s = int(input("Nhap giay:"))
    if 0<h<24 and 0<m<60 and 0<s<60:
        break

k = int(input("Nhap k:"))

if s+k > 59:
    s = (s+k)-60
    m+=1
    if m>59:
        m=0
        h+=1
else:
    s = s+k

print("{0}:{1}:{2}".format(h,m,s))
