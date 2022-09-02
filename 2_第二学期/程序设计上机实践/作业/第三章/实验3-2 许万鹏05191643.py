salary=eval(input("请输入工资:"))
if salary<=400 :
    f=0.005*salary
elif salary<=600 :
    f=0.010*salary
elif salary<=800 :
    f=0.015*salary
elif salary<=1500 :
    f=0.020*salary
else :
    f=0.030*salary
print("应缴纳党费为{:.2f}".format(f))
