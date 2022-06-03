T=int(input())
for o in range(T):
    x,y=map(int,input().split())
    if x-y>1:
        print('YES')
    else:
        print('NO')
