Si=0
for i in range(2,11,2):
    Sj=1
    for j in range(1,i+1):
        Sj=Sj*j
    Si=Si+Sj
print("Si=",Si,sep="")
