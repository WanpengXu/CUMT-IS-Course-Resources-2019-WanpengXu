# -*- coding:cp936 -*-
'''------------------------------------------------------
【程序设计】
---------------------------------------------------------
题目：《射雕英雄传》是金庸的重要武侠作品之一。这里给出一个
      《射雕英雄传》的网络版本的部分内容，文件名为“射雕英雄传-网络版.txt”。
       请编写程序，统计该文件出现的所有中文词语及出现次数（不要求输出）
       ，并输出按照出现次数最多的8个词语，采用如下方式打印输出。

输出示例：词语1，词语2，词语3，词语4，词语5，词语6，词语7，词语8

提示：去掉“\n，。！“”：？”标点符号，结果应显示汉子词语。
---------------------------------------------------------
注意：部分源程序给出如下。请勿改动其它函数中的任何内容，
      仅在函数的注释标志之间填入所编写的若干语句。
------------------------------------------------------'''
fi = open("射雕英雄传-网络版.txt", "r",)
#**********Program**********
'''
txt=fi.read()
import jieba
from collections import Counter
from operator import itemgetter
temp=Counter(jieba.lcut(txt))
for  i in "\n，。！“”：？":
    del temp[i]
temp2=sorted(temp.items(),key=itemgetter(1),reverse=True)
rst=[k for k,v in temp2][:8]
fi.close()
'''
txt=fi.read()
fi.close()#读取完就可以关闭
import jieba
ls=jieba.lcut(txt)
#内建库统计个数，代替Counter
d={}
for i in ls:
    d[i]=d.get(i,0)+1
#删除键值对
for j in "\n，。！“”：？":
    del d[j]
#不使用函数排序
rst=[]
for k in range(8):
    maxvalue=0
    maxkey=0
    for m,n in d.items():
        if n>maxvalue:
            maxvalue=n
            maxkey=m
    rst.append(maxkey)
    del d[maxkey]
#**********  End  **********
print("，".join(rst))
