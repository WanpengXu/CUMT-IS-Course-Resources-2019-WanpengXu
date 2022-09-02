str0=input()
str_set=input().split()
for str in str_set:
    dp=[]
    for i in range(len(str)):
        dp.append(1)# 初始化
        for j in range(i):# 对于第i个字符之前的第j个字符
            if str0.find(str[j])<=str0.find(str[i]):# 如果形成升序
                dp[i]=max(dp[i],dp[j]+1)# 那么该处取 j前的升序串+第i个字符(dp[j]+1)的长度 与 此前该处长度 的较大者
    print(max(dp),end='')