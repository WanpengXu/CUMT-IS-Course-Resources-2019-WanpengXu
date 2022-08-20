#3-9一重循环版
n=eval(input())
S=0
for i in range(1,n+1):
    S+=i*(i+1)//2   #就是手动算通项
print(S)
