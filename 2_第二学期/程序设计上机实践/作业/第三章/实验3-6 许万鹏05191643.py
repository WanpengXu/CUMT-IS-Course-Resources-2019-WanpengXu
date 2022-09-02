from random import randint
a=randint(100,200)
b=randint(100,200)
print("产生的数为{},{}".format(a,b))
m=max(a,b)
n=min(a,b)
r=m%n
while r!=0 :
    m=n
    n=r
    r=m%n
print("这两个数的最大公约数为{}".format(n))
p=a*b//n
print("这两个数的最小公倍数为{}".format(p))
