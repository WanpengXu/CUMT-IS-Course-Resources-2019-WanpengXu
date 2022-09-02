from math import radians,pi,sin
print("这是一个求圆内同角割形的小程序")
r=eval(input("请输入圆的半径\n"))
theta=eval(input("请输入同角的角度（角度制）\n"))
S1=(1/2)*radians(theta)*pow(r,2)
S2=(1/2)*pow(r,2)*sin(radians(theta))
print("所求面积为{:.2f}".format(S1-S2))
