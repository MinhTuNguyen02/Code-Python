from decimal import Decimal
import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,b):
        x0=(b.x-self.x)
        y0=(b.y-self.y)
        d=math.sqrt(x0*x0 + y0*y0)
        return d
    
class Triangle:
    def __init__(self,a=Point,b=Point,c=Point):
        self.a=a
        self.b=b
        self.c=c
    def Perimeter(self):
        ab = self.a.distance(self.b)
        ac = self.a.distance(self.c)
        bc = self.b.distance(self.c)
        if (ab+ac>bc) and (ab+bc>ac) and (bc+ac>ab):
            P=float(ab+ac+bc)
            return "{:.3f}".format(P)
        else:
            return "INVALID"

for i in range(int(input())):
    x1,y1,x2,y2,x3,y3=[float(i) for i in input().split()]
    a=Point(x1,y1) 
    b=Point(x2,y2) 
    c=Point(x3,y3)        
    tri=Triangle(a,b,c)
    print(tri.Perimeter())