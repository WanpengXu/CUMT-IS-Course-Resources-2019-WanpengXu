a=eval(input())
x0=a
x1=(1/2)*(x0+(a/x0))
while abs(x0-x1)>=10e-6 :
    x0,x1=x1,(1/2)*(x1+(a/x1))
print("{:.6f}".format(round(x1,6)))
