#库→类→函数
import datetime
dt=datetime.datetime.now()
print(dt.strftime("%H:%M %Y/%m/%d"))
print(dt.strftime("%p %I:%M %Y/%m/%d"))
print(dt.strftime("%Y-%m-%d %H:%M:%S"))
month=int(dt.strftime("%m"))#eval不允许十进制有前导0
if month<=3 :
    seson="第一季度"
elif month<=6 :
    seson="第二季度"
elif month<=9 :
    seson="第三季度"
else :
    seson="第四季度"
print(seson)
