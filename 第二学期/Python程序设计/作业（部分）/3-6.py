x=eval(input("请输入数x:"))
while True :
    if x%5==0 and x%7==0 and x!=000 :
        print("x能同时被5和7整除")
        x=eval(input("请输入数x:"))
    elif x is 000 :
        break
    else :
        print("x不能同时被5和7整除")
        x=eval(input("请输入数x:"))
print("循环已结束")
input("按任意键退出")
