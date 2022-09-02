w=eval(input("请输入行李重量w（公斤）:"))
if w<=50 :
    y=0.25*w
else :
    y=50*0.25+(w-50)*0.35
print("运费y={}（元）".format(y))
