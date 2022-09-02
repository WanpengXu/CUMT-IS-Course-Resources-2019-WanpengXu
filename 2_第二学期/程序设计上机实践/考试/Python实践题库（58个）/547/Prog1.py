# -*- coding:cp936 -*-
'''------------------------------------------------------
【程序设计】
---------------------------------------------------------
题目：《命运》是著名科幻作家倪匡的科幻作品。这里给出一个
      《命运》的网络版本部分内容，文件名为“命运-网络版.txt”。
       请编写程序，对这个文本中出现的字符进行统计，字符
       与出现次数之间用冒号:分隔，将前10个最常用字符分别
       输出保存到“命运-字符统计.txt”。


注意： 不统计字符包含 \n ，。！：？
    
输出格式：
命:90
运:80
寻:70
梦:60
---------------------------------------------------------
注意：部分源程序给出如下。请勿改动其它函数中的任何内容，
      仅在函数的注释标志之间填入所编写的若干语句。
------------------------------------------------------'''
fi = open("命运-网络版.txt", "r", encoding="utf-8")
fo = open("命运-字符统计.txt", "w")
#**********Program**********
txt=fi.read()
d={}
for i in txt:
    d[i]=d.get(i,0)+1
#应该不能用字典解析，解析法一般都是一一对应的，而统计字符时需要创建新键
for j in "\n ，。！：？":
    del d[j]
#temp=sorted(d.items(),key=lambda x:x[1],reverse=True)
#ls=["{}:{}".format(k,v) for k,v in temp][0:20]
ls=[]
for k in range(10):
    mx=0
    mxj=0
    for m,n in d.items():
        if n>mx:
            mx=n
            mxj=m
    ls.append("{}:{}".format(mxj,mx))
    del d[mxj]
'''
from collections import Counter
from operator import itemgetter
txt=fi.read()
Cd=Counter(txt)

for i in " \n ，。！：？":
    del Cd[i]
temp=sorted(Cd.items(),key=itemgetter(1),reverse=True)
ls=["{}:{}".format(k,v) for k,v in temp][0:20]
'''
#**********  End  **********
fo.write("\n".join(ls[:10]))
fi.close()
fo.close()
