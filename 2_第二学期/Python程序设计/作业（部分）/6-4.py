x=[6,27,33,21,14,9]
m1=str(max(x))
m2=str(min(x))
f=open("D:\\date4.txt","w")
f.write(m1+"\n"+m2+"\n")
f.close()#不关闭就写不了值
