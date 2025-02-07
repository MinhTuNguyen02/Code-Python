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
        return "{:.4f}".format(d)


n=int(input())
for i in range(n):
    x1,y1,x2,y2=[Decimal(i) for i in input().split()]
    a=Point(x1,y1)
    b=Point(x2,y2)
    print(a.distance(b))