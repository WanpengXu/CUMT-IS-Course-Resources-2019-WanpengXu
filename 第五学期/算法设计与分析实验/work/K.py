n=int(input())
a=[0]+[int(_) for _ in input().split()]
dp=[1]*(n+1)
last=[-1]*(n+1)# 前趋数组
for i in range(1,n+1):
    for j in range(1,i):# 这里正着反着都行，因为前面已经存好了
        if a[j]>a[i] and dp[j]+1>dp[i]:# 递减+打擂（这里不用max是因为还要顺便存前趋，下同）
            dp[i]=dp[j]+1
            last[i]=j# 很重要！！
ans=0# 最优解的长度
ansp=1# 最优解的的末端指针
for i in range(1,n+1):
    if dp[i]>ans:# 打擂
        ans=dp[i]
        ansp=i
# 构造最优解
ansa=[0]*(ans+1)# 最优解本身
i=ans
j=ansp
while True:
    ansa[i]=a[j]# 从后往前构造
    if last[j]==-1:
        break
    j=last[j]
    i-=1
print(' '.join(map(str,ansa[1:])))