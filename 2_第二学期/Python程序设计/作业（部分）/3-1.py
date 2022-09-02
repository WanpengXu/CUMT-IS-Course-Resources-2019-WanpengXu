x=eval(input("请输入购买金额:"))
while x<0 :
    print("请输入正确的数字")
    x=eval(input("请输入购买金额:"))
if x<1000 :
    y=x
elif x<2000 :
    y=0.95*x
elif x<3000 :
    y=0.9*x
elif x<5000 :
    y=0.85*x
else :
    y=0.8*x
print("您的实付金额为{:.2f}".format(y))
