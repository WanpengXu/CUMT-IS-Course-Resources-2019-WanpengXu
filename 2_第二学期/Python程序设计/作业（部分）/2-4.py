from math import pi
print("提示：请注意单位统一")
r=eval(input("请输入圆柱体半径:"))
h=eval(input("请输入圆柱体高:"))
S=2*pi*r*h
V=pi*pow(r,2)*h
print("圆柱体的表面积为:",round(S,2))
print("圆柱体的体积为:",round(V,2))
