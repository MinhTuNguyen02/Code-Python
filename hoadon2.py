import datetime
class KhachHang:
    stt=1
    def __init__(self,ten,phong,nhan,tra,dv):
        self.ten=ten
        self.phong=phong
        s=nhan.split('/')
        self.nhan=datetime.date(int(s[2]),int(s[1]),int(s[0]))
        s=tra.split('/')
        self.tra=datetime.date(int(s[2]),int(s[1]),int(s[0]))
        self.dv=dv
        if KhachHang.stt<10:
            self.ma='KH0'+str(KhachHang.stt)
        else:
            self.ma='KH'+str(KhachHang.stt)
        KhachHang.stt+=1
    def tinhngay(self):
        return (self.tra-self.nhan).days+1
    def tinhtien(self):
        ngay=self.tinhngay()
        tang=int(self.phong[0])
        tien=0
        if tang==1:
            tien=25*ngay+self.dv
        elif tang ==2:
            tien=34*ngay+self.dv
        elif tang==3:
            tien=50*ngay+self.dv
        elif tang==4:
            tien=80*ngay+self.dv
        return int(tien)
    def __str__(self):
        return f'{self.ma} {self.ten} {self.phong} {self.tinhngay()} {self.tinhtien()}'

a=[]
for i in range(int(input())):
    ten=input()
    phong=input()
    nhan=input()
    tra=input()
    dv=int(input())
    a.append(KhachHang(ten,phong,nhan,tra,dv))
a.sort(key=lambda x: x.tinhtien(),reverse=True)
for i in a:
    print(i)

    
