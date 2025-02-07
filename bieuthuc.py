for x in range(int(input())):
    s=input()
    count=0
    a=[]
    for i in s:
        if i=='(':
            count+=1
            a.insert(0,count)
            print(count,end=" ")
        if i==')':
            print(a[0],end=" ")
            a.pop(0)
    print()
 