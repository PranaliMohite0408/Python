def ChkPrime(Num):    
    Cnt=0
    for i in range(2,Num):
        if(Num%i==0):
            Cnt = Cnt+1
                   
    if(Cnt != 0):
        return "Number is Not Prime"
    else:
        return "Number is Prime"
    