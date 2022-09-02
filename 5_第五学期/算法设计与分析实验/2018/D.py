vight,n,c=map(int,input().split())
w=[0]
v=[0]
for _ in range(n):
    _v,_w=map(int,input().split())
    w.append(_w)
    v.append(_v)

dp=[[0]*(c+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,c+1):
        dp[i][j]=dp[i-1][j]
        if j>=w[i]:
            dp[i][j]=max(dp[i][j],dp[i-1][j-w[i]]+v[i])

if dp[-1][-1]<vight:# 没有偷到目标价值的东西（没完成葬花）
    print('NO')
else:
    t=c
    for i in range(n,0,-1):
        if dp[i][t]==dp[i-1][t]:
            t-=0
        else:
            t-=w[i]
    print(t)