def is_valid_cccd(cccd=''):
    cccd=list(cccd[::-1])
    for i in range(0,len(cccd),2):
        cccd[i]=int(cccd[i])*2
        if int(cccd[i])>9:
            cccd[i]=(int(cccd[i])-9)
    res=0
    for i in cccd:
        res+=int(i)
  
    return res%10==0

def get_all_cccd(atm):
    cccd_list=[]
    for i in range(0,10):
        tmp=atm+str(i)
        if is_valid_cccd(tmp):
            cccd_list.append(tmp)
    return cccd_list


print(is_valid_cccd('074204000900'))
a=get_all_cccd('07420400090')
print(*a,sep="\n")

