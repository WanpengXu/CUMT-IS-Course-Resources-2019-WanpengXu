# -*- coding:cp936 -*-
'''------------------------------------------------------
【程序设计】
---------------------------------------------------------

题目：补充函数getLastDay(y,m)，其功能是计算y年m月共有多少天。

---------------------------------------------------------
注意：部分源程序给出如下。请勿改动主函数main和其它函数中的
      任何内容，仅在函数的注释标志之间填入所编写的若干语句。
------------------------------------------------------'''
def getLastDay(y,m):
    #**********Program**********
     '''
     m1=[1,3,5,7,8,10,12]
     m2=[4,6,9,11]
     if m in m1:
          return 31
     elif m in m2:
          return 30
     else :
          if leapYear(y):
               return 29
          else:
               return 28
     '''
     if y<1:
          y=1
     if m<1:
          m=1
     elif m>12:
          m=12
     monthDay=[31,28,31,30,31,30,31,31,30,31,30,31]
     r=monthDay[m-1]
     if m==2:
          r+=leapYear(y)
     return r

    #**********  End  **********

def  leapYear( y ):
     if y<1:
         y=1
     if (y % 400)== 0:
         lp = 1
     elif (y % 100)== 0:
         lp=0
     elif (y % 4)==0:
          lp =1
     else:
         lp = 0
     return lp

def main():
    print("【请分别三次计算某年某月共有多少天：】")
    for n in range(3):
        print("【第%d次：】" %(n+1))
        y = int(input("【请输入年份y：】"))
        m = int(input("【请输入月份m：】"))
        print(getLastDay(y,m))
    
if __name__ == '__main__':
    main()

