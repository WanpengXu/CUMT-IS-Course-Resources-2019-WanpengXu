f=open("sy6-6.txt",'r+')
#num=len(f.readlines())
scores={}
for i in range(0,6):
    temp=f.readline(-1)
    temp=temp.split(" ")
    tempscores=[eval(i) for i in temp[1:]]
    tempaverage=(sum(tempscores)-max(tempscores)-min(tempscores))/8
    scores.update({temp[0]:tempaverage})
rank=sorted(scores.items(),key=lambda value:value[1],reverse=True)
for k,v in rank:
    print(k,v)
    '''
    f.write("\n")
    f.write(k+" "+str(v))
    '''
f.close()

