import random
a=random.randint(100,999)
b=random.randint(100,999)
c=random.randint(100,999)
if a>=b :
    if a>=c :
        if b>=c :
            x,y,z=c,b,a
        else :
            x,y,z=b,c,a
    else :
        x,y,z=b,a,c
else :
    if a>=c :
        x,y,z=c,b,a
    else :
        if b>=c:
            x,y,z=a,c,b
        else :
            x,y,z=a,b,c
print("三数从小到大排列为:{}、{}、{}".format(x,y,z))
        
