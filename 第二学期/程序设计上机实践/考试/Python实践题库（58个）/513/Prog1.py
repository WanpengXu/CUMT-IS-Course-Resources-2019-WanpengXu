# -*- coding:cp936 -*-
'''------------------------------------------------------
【程序设计】
---------------------------------------------------------
题目：使用 turtle 库绘制同心圆图形，效果如样张1所示。
      阅读程序框架，补充横线处代码。
---------------------------------------------------------
注意：部分源程序给出如下。请勿改动其它函数中的任何内容，
      仅在函数的注释标志之间填入所编写的若干语句。
      先将程序段中横线部分去掉，然后填写正确的程序内容
------------------------------------------------------'''
#**********Program**********

import turtle as t
def DrawCctCircle(n):
    t.penup()
    t.goto(0,-n)
    t.pendown()
    t.circle(n)

#**********  End  **********
for i in range(20,100,20):
    DrawCctCircle(i)
t.hideturtle()
t.done()



