class NhanVien:
    stt=1
    def __init__(self,ten,lt,tt):
        lt = lt if lt<=10 else lt/10
        tt = tt if tt<=10 else tt/10
        if NhanVien.stt<10:
            self.ma="TS0"+str(NhanVien.stt)
        else:
            self.ma="TS"+str(NhanVien.stt)
        self.ten=ten
        self.lt=lt
        self.tt=tt
        NhanVien.stt+=1
    def trungBinh(self):
        return (self.tt+self.lt)/2
    def xepLoai(self):
        tb = self.trungBinh()
        if tb <5:
            return "TRUOT"
        elif tb<8:
            return "CAN NHAC"   
        elif tb<9.5:
            return "DAT"
        else:
            return "XUAT SAC"
    def __str__(self):
        return f"{self.ma} {self.ten} {'%.2f'%self.trungBinh()} {self.xepLoai()}"


a=[]    
for i in range(int(input())):
    ten=input()
    lt=float(input())
    tt=float(input())
    a.append(NhanVien(ten,lt,tt))
a.sort(key=lambda x : x.trungBinh(),reverse=True)
for i in a:
    print(i)
