s1,s2=input().split()
m=len(s1)
n=len(s2)
dp=[[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if s1[i-1]==s2[j-1]:# 这里要注意一下，要么从1起，字符串前面补0，要么从0起，循环变量-1
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])