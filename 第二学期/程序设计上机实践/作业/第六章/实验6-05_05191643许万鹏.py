import random
f=open("sy6-5.txt",'w')
count=0
for i in range(1,21):
    f.write(str(random.random())+' ')
    if i%5==0:
        f.write("\n")
f.close()
    
