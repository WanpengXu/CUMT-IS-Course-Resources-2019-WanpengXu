year,month=eval(input("请输入年份和月份，数据间以逗号相隔："))
month1=[1,3,5,7,8,10,12]
month2=[4,6,9,11]
if month<1 or month>12 or year<0 :
    print("年份或者月份不合法！")
else :
    print("{}年{}月有".format(year,month),end="")
    if month in month1 :
        print("31天")
    elif month in month2 :
        print("30天")
    else :
        if year%400==0 or year%4==0 and year%100!=0 :
            print("29天")
        else :
            print("28天")
