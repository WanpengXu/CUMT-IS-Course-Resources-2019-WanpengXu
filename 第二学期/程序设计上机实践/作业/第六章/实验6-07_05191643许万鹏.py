f=open("sy6-7.txt","r")
info=[i.split(',') for i in f.readlines()]
infodic=dict(info)
name=input()
if name in infodic:
    print(infodic[name].replace("\n",''))
else:
    print("查无此人")
f.close()
