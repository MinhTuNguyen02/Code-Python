class KhachHang:
    stt=1
    def __init__(self,ten,cu,moi):
        self.ten=ten
        self.cu=cu
        self.moi=moi
        if KhachHang.stt<10:
            self.ma='KH0'+str(KhachHang.stt)
        else:
            self.ma='KH'+str(KhachHang.stt)
        KhachHang.stt+=1
    def tinhtien(self):
        nuoc=self.moi-self.cu 
        tien=0
        if nuoc<=50:
            tien=nuoc*100*102/100
        elif nuoc<=100:
            tien=(50*100 + (nuoc-50)*150)*103/100
        else:
            tien=(50*100 + 50*150 + (nuoc-100)*200)*105/100
        return int(tien)
    def __str__(self):
        return f'{self.ma} {self.ten} {self.tinhtien()}'

a=[]
for i in range(int(input())):
    ten=input()
    cu=int(input())
    moi=int(input())
    a.append(KhachHang(ten,cu,moi))
a.sort(key=lambda x: x.tinhtien(),reverse=True)
for i in a:
    print(i)
f=open("test.txt",'w')
for i in a:
    f.write(str(i)+'\n')
f.close

