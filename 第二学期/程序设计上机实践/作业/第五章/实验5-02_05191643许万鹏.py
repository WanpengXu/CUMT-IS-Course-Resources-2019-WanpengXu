def eachprime(x,y):
    '''judge eachprime whether or not'''
    #公因数只有1的两个非零自然数，叫做互质数
    '''if x%y==0 or y%x==0 :
        return True
    else :
        return False'''
    temp=x%y
    while temp!=0:
        x=y
        y=temp
        temp=x%y
    if y==1 :
        return True
    else :
        return False

if __name__=="__main__":
    from random import randint
    a,b=randint(1,100),randint(1,100)
    print(a,b)
    print(eachprime(a,b))
