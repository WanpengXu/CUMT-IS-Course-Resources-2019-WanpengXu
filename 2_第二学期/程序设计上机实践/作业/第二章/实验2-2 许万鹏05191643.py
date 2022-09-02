from math import pi
print("请注意单位转换")
r=eval(input("请输入球的半径"))
while r<=0 :
    print("请输入正确的半径")
    r=eval(input("r="))
S=4*pi*pow(r,2)
V=(4/3)*pi*pow(r,3)
print("球的表面积为{0:.2f}，体积为{1:.2f}".format(S,V))
