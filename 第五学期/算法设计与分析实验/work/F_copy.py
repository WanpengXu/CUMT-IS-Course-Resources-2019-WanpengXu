def LIS(nums):
    dp=[]
    for i in range(len(nums)):
        dp.append(1)
        for j in range(i):
            if nums[j]<nums[i]:
                dp[i]=max(dp[i],dp[j]+1)
    return dp

while True:
    n=int(input())
    a=[int(i) for i in input().split()]
    dp=LIS(a)
    dpr=LIS(a[::-1])[::-1]
    ans=1
    for i in range(n):
        if min(dp[i],dpr[i])>ans:
            ans=min(dp[i],dpr[i])
    print(2*ans-1)