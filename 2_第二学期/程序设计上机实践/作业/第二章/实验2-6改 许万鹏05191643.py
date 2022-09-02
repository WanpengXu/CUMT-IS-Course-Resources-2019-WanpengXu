from math import radians,sin
r=2
theta=110
S1=(1/2)*radians(theta)*pow(r,2)
S2=(1/2)*pow(r,2)*sin(radians(theta))
print("6题所求面积为{:.2f}".format(S1-S2))
