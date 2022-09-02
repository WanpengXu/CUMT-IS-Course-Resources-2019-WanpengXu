n=int(input())
A=[int(_) for _ in input().split()]
sum=float('-inf')
dp=float('-inf')
for a in A:
    dp=max(dp+a,a)
    sum=max(sum,dp)
print(sum)