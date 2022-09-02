N=int(input())
dp=[[0]*(N+1)]
for i in range(1,N+1):
    dp_row=[0]+[int(_) for _ in input().split()]
    dp_row+=[0]*(N-i)
    dp.append(dp_row)
for i in range(N-1,1-1,-1):# 从第N-1行往上加一直到第1行
    for j in range(1,i+1):# 从第1列到第i列
        dp[i][j]+=max(dp[i+1][j],dp[i+1][j+1])
print(dp[1][1])