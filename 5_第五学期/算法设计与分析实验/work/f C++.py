# MLE 83%
# 只能用C++！！！！！！！
OFFSET=500000
MAXN=1000000+5
Hash=[0]*MAXN
while True:
    n,m=map(int,input().split())
    for i in range(-500000,500000+1):
        Hash[i+OFFSET]=0
    a=[int(_) for _ in input().split()]
    for x in a:
        Hash[x+OFFSET]+=1
    # print(Hash[1+OFFSET:9+OFFSET])
    for i in range(500000,-500000-1,-1):
        if m==0:
            break
        while Hash[i+OFFSET]:
            Hash[i+OFFSET]-=1
            print(i,end='')
            m-=1
            if m>0:
                print(' ',end='')
            else:
                print()
                break