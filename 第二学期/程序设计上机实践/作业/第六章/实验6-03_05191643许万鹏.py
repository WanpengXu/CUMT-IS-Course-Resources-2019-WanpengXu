f=open("sy6-3.txt","r")
info=f.readlines()
average=[]
temp=[]
num1=len(info[0].split(','))-1#科目数
num2=len(info)#人数
for i in range(1,num1+1):
    for j in range(0,num2):
        lineinfo=info[j].split(",")
        temp.append(lineinfo[i])
    temp=[eval(k) for k in temp]
    average.append(sum(temp)/num2)
    temp=[]
print(average)
f.close()
