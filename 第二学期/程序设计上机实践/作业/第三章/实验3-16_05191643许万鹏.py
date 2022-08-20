x=eval(input())
n=0
ex=0
f=1
while f>=1e-6 :
    J=1
    for i in range(1,n+1):
        J*=i
    f=pow(x,n)/J
    n+=1
    ex+=f
print(ex)
