n,m=map(int,input().split())
a=[int(_) for _ in input().split()]
a.sort(reverse=True)
for i in range(m):
    print(a[i],end=' ')