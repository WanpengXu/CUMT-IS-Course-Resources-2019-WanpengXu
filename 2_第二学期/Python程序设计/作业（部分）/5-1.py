def isprime(x):
    if x==1:
        return False     
    for j in range(2,x):
        if x%j==0:
            return False
    return True

a,b =map(int,input().split())
S=0
for i in range (a,b+1):
    if isprime(i):
        print("{}*{}+".format(i,i),end='')#"+",i,"*",i,sep='',end='')
        S+=pow(i,2)
print("\b=",S,sep='')
input()
    
