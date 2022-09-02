T=int(input())
while True:
    if T==0:
        break
    T-=1

    c,n=map(int,input().split())
    w=[0]
    v=[0]
    for _ in range(n):
        _w,_v=map(int,input().split())
        w.append(_w)
        v.append(_v)

    # 从上往下的背包
    dp=[[0]*(c+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,c+1):
            dp[i][j]=dp[i-1][j]
            if j>=w[i]:
                dp[i][j]=max(dp[i][j],dp[i-1][j-w[i]]+v[i])
    print(dp[-1][-1])

    # 从下往上的背包，为满足公式需要多添一行，否则就要像传统代码一样先对最后一行赋值
    # dp=[[0]*(c+2) for _ in range(n+2)]
    # for i in range(n,1-1,-1):
    #     for j in range(1,c+1):
    #         dp[i][j]=dp[i+1][j]
    #         if j>=w[i]:
    #             dp[i][j]=max(dp[i][j],dp[i+1][j-w[i]]+v[i])
    # print(dp[1][c])