for i in range(100,1000):
    a=i%10
    b=(i//10)%10
    c=i//100
    if pow(a,3)+pow(b,3)+pow(c,3)==i :
        print(i,end=',')
#可用循环嵌套改进
