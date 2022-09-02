import random
a=random.randint(100,999)
b=random.randint(100,999)
c=random.randint(100,999)
if a<=b<=c:
    print("三数从小到大排列为:{}、{}、{}".format(a,b,c))
elif a<=c<=b:
    print("三数从小到大排列为:{}、{}、{}".format(a,c,b))
elif b<=a<=c:
    print("三数从小到大排列为:{}、{}、{}".format(b,a,c))
elif b<=c<=a:
    print("三数从小到大排列为:{}、{}、{}".format(b,c,a))
elif c<=a<=b:
    print("三数从小到大排列为:{}、{}、{}".format(c,a,b))
else :
    print("三数从小到大排列为:{}、{}、{}".format(c,b,a))
