n,c=map(int,input().split())
w=[0]
v=[0]
for _ in range(n):
    _w,_v=map(int,input().split())
    w.append(_w)
    v.append(_v)
dp=[[0]*(c+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,c+1):
        dp[i][j]=dp[i-1][j]
        if j>=w[i]:
            dp[i][j]=max(dp[i][j],dp[i-1][j-w[i]]+v[i])
print(dp[-1][-1])