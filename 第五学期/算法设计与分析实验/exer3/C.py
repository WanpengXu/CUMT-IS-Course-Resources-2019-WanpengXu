n=int(input())
A=[int(_) for _ in input().split()]
dp=float('-inf')
m=float('-inf')
for a in A:
    dp=max(dp+a,a)
    m=max(m,dp)
print(m)