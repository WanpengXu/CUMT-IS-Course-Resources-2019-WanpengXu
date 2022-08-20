'''for i in range(1,1001):
    j=str(pow(i,2))
    i=str(i)
    if j.rfind(i)!=-1 :
        print(i,end=",")
    这是想弄一个自动判别位数并利用字符串查找的程序
'''
for i in range(1,1001):
    j=pow(i,2)
    if i<=9 :
        if i==j%10 :
            print(i,end=",")
    elif i<=99 :
        if i==j%100 :
            print(i,end=",")
    else :
        if i==j%1000 :
            print(i,end=",")
