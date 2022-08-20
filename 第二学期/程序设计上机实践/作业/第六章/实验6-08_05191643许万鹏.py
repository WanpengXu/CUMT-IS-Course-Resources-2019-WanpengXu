print("提示错误请尝试直接双击或使用32-bit模式")
#from collections import Counter
import jieba
f=open("sy6-8.txt","r")
txt=f.read(-1)
words=jieba.lcut(txt)
result={}
for key in words:
    result[key]=result.get(key,0)+1
#result=Counter(words)
sortedresult=sorted(result.items(),key=lambda x:x[1],reverse=True)
print("{}\n{}\n{}\n{}\n{}".format(sortedresult[0],sortedresult[1],sortedresult[2],sortedresult[3],sortedresult[4],sortedresult[5]))
input()
