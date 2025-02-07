def is_arms(n):
    m=str(n)
    res=0
    for i in m:
        res+=int(i)**len(m)
    return res==n

def list_n_arms(n):
    a=[]
    i=0
    while len(a)<n:
        if is_arms(i):
            a.append(i)
        i+=1
    return a

def get_arms(my_list=[]):
    a=list(set(my_list))
    b=[]
    i=0
    while 1:
        if is_arms(a[i]):
            b.append(a[i])
        i+=1
        if i==len(a): break
    b.sort()
    return b

def main():
    print(is_arms((0)))
    print(list_n_arms(20))
    my_list = [0,34,56,2,34,6,4857,466,153,777,3,370,2,5,8,6,1634,6666,3,371]
    print(get_arms(my_list))

if __name__=='__main__':
    main()