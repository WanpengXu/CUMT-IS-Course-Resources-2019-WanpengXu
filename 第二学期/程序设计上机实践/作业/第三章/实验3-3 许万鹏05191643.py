a,b,c=eval(input("请输入三条边，数据间以逗号相隔："))
if a<=0 or b<=0 or c<=0 :
    print("数据不合法！")
elif a+b<=c or a+c<=b or b+c<=a :
    print("不能构成三角形！")
else :
    h=(1/2)*(a+b+c)
    s=pow(h*(h-a)*(h-b)*(h-c),(1/2))
    print("三角形的面积：{:.2f}".format(s))
