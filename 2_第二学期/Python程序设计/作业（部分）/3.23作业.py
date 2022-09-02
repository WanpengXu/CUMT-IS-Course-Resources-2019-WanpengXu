a=input()
flag=a.find("love")
S=0
while flag!=-1 :
    print(a.find("love"),end=",")
    S+=1
    a=a.replace("love","hope",1)
    flag=a.find("love")
print("\n",S,sep="")
print(a)
'''

a=input()
S=0
b=a.split(" ")
for i in b:
    if "love" in i :
        print(a.find("love"),end=",")
        S+=1
        a=a.replace("love","hope",1)
print()
print(S)
print(a)

'''
#列表方案还是有问题

