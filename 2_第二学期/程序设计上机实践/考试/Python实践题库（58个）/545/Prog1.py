# -*- coding:cp936 -*-
'''------------------------------------------------------
��������ơ�
---------------------------------------------------------
��Ŀ�������Ӣ�۴����ǽ�ӹ����Ҫ������Ʒ֮һ���������һ��
      �����Ӣ�۴���������汾�Ĳ������ݣ��ļ���Ϊ�����Ӣ�۴�-�����.txt����
       ���д����ͳ�Ƹ��ļ����ֵ��������Ĵ��Ｐ���ִ�������Ҫ�������
       ����������ճ��ִ�������8������������·�ʽ��ӡ�����

���ʾ��������1������2������3������4������5������6������7������8

��ʾ��ȥ����\n���������������������ţ����Ӧ��ʾ���Ӵ��
---------------------------------------------------------
ע�⣺����Դ����������¡�����Ķ����������е��κ����ݣ�
      ���ں�����ע�ͱ�־֮����������д��������䡣
------------------------------------------------------'''
fi = open("���Ӣ�۴�-�����.txt", "r",)
#**********Program**********
'''
txt=fi.read()
import jieba
from collections import Counter
from operator import itemgetter
temp=Counter(jieba.lcut(txt))
for  i in "\n��������������":
    del temp[i]
temp2=sorted(temp.items(),key=itemgetter(1),reverse=True)
rst=[k for k,v in temp2][:8]
fi.close()
'''
txt=fi.read()
fi.close()#��ȡ��Ϳ��Թر�
import jieba
ls=jieba.lcut(txt)
#�ڽ���ͳ�Ƹ���������Counter
d={}
for i in ls:
    d[i]=d.get(i,0)+1
#ɾ����ֵ��
for j in "\n��������������":
    del d[j]
#��ʹ�ú�������
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
print("��".join(rst))
