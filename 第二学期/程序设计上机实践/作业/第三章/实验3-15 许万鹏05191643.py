x1,x2,x3=1,2,3
N=3
while x3<=2000 :
    x1,x2,x3=x2,x3,x1+x2+x3
    N+=1
print(N)
