#from math import ceil,sqrt
S=0
for i in range(2,101):
    flag=True
    for j in range(2,i):#    for j in range(2,ceil(sqrt(i+1))):
        if i%j==0 :
            flag=False
    if flag is True :
        S+=i
print(S)
