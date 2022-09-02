n,l=map(int,input().split())
ls=[int(_) for _ in input().split()]
ls.sort(reverse=True)
sum=0
for li in ls[:-1]:
    sum+=l# 锯断当前l，增加花费
    l-=li# l减小被锯断的长度
print(sum)