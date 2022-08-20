S=0
a=eval(input("请输入数列首项:"))
d=eval(input("请输入数列公差:"))
n=eval(input("请输入欲计算项数:"))
b=a+(n-1)*d+1
for i in range(a,b,d) :
    S=S+i
print("该数列和S=",S)
