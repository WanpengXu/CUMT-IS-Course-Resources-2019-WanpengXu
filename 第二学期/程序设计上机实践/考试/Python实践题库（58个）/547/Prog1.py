# -*- coding:cp936 -*-
'''------------------------------------------------------
��������ơ�
---------------------------------------------------------
��Ŀ�������ˡ��������ƻ������߿�Ŀƻ���Ʒ���������һ��
      �����ˡ�������汾�������ݣ��ļ���Ϊ������-�����.txt����
       ���д���򣬶�����ı��г��ֵ��ַ�����ͳ�ƣ��ַ�
       ����ִ���֮����ð��:�ָ�����ǰ10������ַ��ֱ�
       ������浽������-�ַ�ͳ��.txt����


ע�⣺ ��ͳ���ַ����� \n ����������
    
�����ʽ��
��:90
��:80
Ѱ:70
��:60
---------------------------------------------------------
ע�⣺����Դ����������¡�����Ķ����������е��κ����ݣ�
      ���ں�����ע�ͱ�־֮����������д��������䡣
------------------------------------------------------'''
fi = open("����-�����.txt", "r", encoding="utf-8")
fo = open("����-�ַ�ͳ��.txt", "w")
#**********Program**********
txt=fi.read()
d={}
for i in txt:
    d[i]=d.get(i,0)+1
#Ӧ�ò������ֵ������������һ�㶼��һһ��Ӧ�ģ���ͳ���ַ�ʱ��Ҫ�����¼�
for j in "\n ����������":
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

for i in " \n ����������":
    del Cd[i]
temp=sorted(Cd.items(),key=itemgetter(1),reverse=True)
ls=["{}:{}".format(k,v) for k,v in temp][0:20]
'''
#**********  End  **********
fo.write("\n".join(ls[:10]))
fi.close()
fo.close()
