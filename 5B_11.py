def ucln(a,b):
    while a*b!=0:
        if a>b:
            a %= b
        else:
            b %= a
    return a+b

a=int(input())
b=int(input())
print(ucln(a,b))



