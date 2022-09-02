N=int(input())
a=[0]+[int(_) for _ in input().split()]
sum=[0]
for i in range(1,N+1):
    sum.append(sum[i-1]+a[i])
dp=[[0]*(N+1) for _ in range(N+1)]
for length in range(1,N+1):
    for i in range(1,N-length+1):# i+length<=N
        j=i+length
        dp[i][j]=float('inf')
        for k in range(i,j):
            dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+(sum[j]-sum[i-1]))
print(dp[1][N])