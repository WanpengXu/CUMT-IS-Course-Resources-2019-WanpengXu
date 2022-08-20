print("这是一个逆序程序")
x=eval(input("请输入一个不超过三位的正整数"))
while x<=0 or x>999 :
    print("请输入正确的数字")
    x=eval(input("x="))
print("您输入的数字为{:0>3d}".format(x))
a=x//100
b=x//10-a*10
c=x%10
y=c*100+b*10+a
print("所得结果为{}".format(y))
