a=0 #从1-100跳7的数字

while a<100:
    a+=1
    if a%7==0:#7的倍数
        pass
    elif a%10==7:#各位上有7
        pass
    elif a//10==7:#十位数上有7
        pass
    else:
        print(a)
   
        

print(1+1)