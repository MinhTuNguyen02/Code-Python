x=int(input())
n=int(input())
sum=0
for i in range(0,n+1):
    sum += x**(2*i+1)
print(sum)