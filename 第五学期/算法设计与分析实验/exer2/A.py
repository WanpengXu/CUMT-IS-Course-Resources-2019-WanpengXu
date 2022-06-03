N=int(input())
_a=[int(_) for _ in input().split()]
dp=[[0]*(N+1) for _ in range(N+1)]# 从第i个合并到第i个的代价（搬运多次 i——>i 的代价）
a=[0]+_a
s=[0]# 从第1个合并到第i个的代价（搬运一次 1——>i 的代价）（沙子本身的重量之和）
for i in range(1,N+1):
    s.append(s[i-1]+a[i])
for length in range(1,N):# 长度
    for i in range(1,N-length+1):# 左端点 i+length<=n
        j=i+length# 右端点
        dp[i][j]=float('inf') # 初值
        for k in range(i,j):# 断点
            dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+(s[j]-s[i-1]))
print(dp[1][N])

for i in dp:
    print(i)
print(s)