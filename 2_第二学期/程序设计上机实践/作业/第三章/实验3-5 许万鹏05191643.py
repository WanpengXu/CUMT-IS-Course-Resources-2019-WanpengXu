a,b,c=eval(input())
if a==0 and b==0 :
    print("数据不合法!")
elif a==0 and b!=0 :
    x=-c/b
    print(x)
else :
    delta=pow(b,2)-4*a*c
    if delta>=0 :
        x1=(-b-pow(delta,1/2))/(2*a)
        x2=(-b+pow(delta,1/2))/(2*a)
    else :
        from cmath import sqrt
        x1=(-b-sqrt(delta))/(2*a)
        x2=(-b+sqrt(delta))/(2*a)
    print(x1,x2)
