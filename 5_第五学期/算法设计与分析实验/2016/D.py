t=int(input())
for o in range(t):
    m,n=map(int,input().split())
    w=[int(_) for _ in input().split()]
    w.sort()
    ans=0
    for i in w:
        if i<=m:
            m-=i
            ans+=1
    print(ans)