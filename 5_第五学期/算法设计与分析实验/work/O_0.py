n=int(input())
A=[int(_) for _ in input().split()]
sum=float('-inf')
dp=float('-inf')
for i in range(n):
    if dp>0:
        dp+=A[i]
    else:
        dp=A[i]
    if dp>sum:
        sum=dp
print(sum)