# -*- coding:cp936 -*-
'''------------------------------------------------------
【程序设计】
---------------------------------------------------------
题目：输出如下数列在 1000000 以内的值，以逗号分隔：k(0)= 1,
      k(1)=2, k(n) = k(n–1)**2 + k(n–2)**2，其中，k(n) 表示
      该数列第n项的值。 
---------------------------------------------------------
注意：部分源程序给出如下。请勿改动其它函数中的任何内容，
      仅在函数的注释标志之间填入所编写的若干语句。
------------------------------------------------------'''

#**********Program**********
def k(n):
    if n==0:
        return 1
    elif n==1:
        return 2
    else:
        return k(n-1)**2+k(n-2)**2
i=0
while True:
    if k(i)<1000000:
        print(k(i),end=',')
        i+=1
    else:
        break





#**********  End  **********

