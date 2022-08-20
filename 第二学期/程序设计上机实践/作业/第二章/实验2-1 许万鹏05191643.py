print("请注意单位转换")

v1=eval(input("请输入汽车的初始速度（公里/小时）"))
while v1<=0 :
    print("请输入正确的初始速度")
    v1=eval(input("请输入汽车的初始速度（公里/小时）"))

t=eval(input("请输入汽车的加速时间（秒）"))
while t<=0 :
    print("请输入正确的加速时间")
    t=eval(input("请输入汽车的加速时间（秒）"))

v2=eval(input("请输入汽车的最终速度（公里/小时）"))
while v2<=0 :
    print("请输入正确的初始速度")
    v2=eval(input("请输入汽车的最终速度（公里/小时）"))

a=((v2/3.6)-(v1/3.6))/t
print("平均加速度a={0:.2f}{1}".format(a,"（米/秒^2）"))
