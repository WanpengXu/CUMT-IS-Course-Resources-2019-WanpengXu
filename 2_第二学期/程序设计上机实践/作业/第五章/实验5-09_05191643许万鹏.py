def sonlistsum(x):
    y=pow(x,3)
    fatherlist=list(range(1,y+1,2))
    i=0
    while i<len(fatherlist):
        sonlist=fatherlist[i:i+x]
        if sum(sonlist)==y:
            return sonlist
        i+=1
    return []

if __name__=="__main__":
    n=int(input())
    nlist=sonlistsum(n)
    if nlist==[]:
        print("是假命题")
    else:
        for j in range(1,n+1):
            nlist=sonlistsum(j)
            sonliststr=[str(i) for i in nlist]
            print("{}**3={}".format(j,"+".join(sonliststr)))
