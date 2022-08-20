# -*- coding:cp936 -*-
'''------------------------------------------------------
【程序设计】
---------------------------------------------------------
题目：《笑傲江湖》是金庸的重要武侠作品之一。这里给出一个
      《笑傲江湖》的网络版本的部分内容，文件名为“笑傲江湖-网络版.txt”。
       请编写程序，统计“笑傲江湖-网络版.txt”中出现在引号内
       所有字符占文本总字符的比例，如输出示例格式所示：
       用程序运行结果的真实数字替换上述示例中数字，均保留整数，
       字符串中标点符号采用中文字符。

输出示例：
   
【占总字符比例：】20%
---------------------------------------------------------
注意：部分源程序给出如下。请勿改动其它函数中的任何内容，
      仅在函数的注释标志之间填入所编写的若干语句。
------------------------------------------------------'''

fi = open("笑傲江湖-网络版.txt", "r")

#**********Program**********
txt=fi.read()
cnt=0
flag=False
for i in txt:
    if i == '“':
        flag=True
        continue
        #不加continue的话下面会+=1，也即算进了左引号
    elif i=='”':
        flag=False
    if flag:
        cnt+=1




#**********  End  **********

print("【占总字符比例：】{:.0%}".format(cnt/len(txt)))
fi.close()
