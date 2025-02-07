import math
mu=[]
hs=[]
while True:
    n=int(input("Nhập số mũ hoặc -1 để kết thúc:"))
    if n==-1:
        break
    else:
        a=float(input("Nhập hệ số của x^{0}:".format(n)))
        mu.append(n)
        hs.append(a)
print("P = ",end="")
for i in range(len(mu)):
    print(" + {0}*x^{1}".format(hs[i],mu[i]),end="")
x=int(input("\nNhập x để tính giá trị đa thức tại x:"))
sum=0
for i in range(len(mu)):
    sum += hs[i]*math.pow(x,mu[i])
print("Giá trị của đa thức tại x={0} là {1}".format(x,sum))

        
