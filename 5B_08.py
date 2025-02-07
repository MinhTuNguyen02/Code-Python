n = input()
l = len(n)
sum=0
for i in range(l):
    sum += int(n[i])

print("So luong chu so: {0}, tong cac chu so: {1}".format(l,sum))