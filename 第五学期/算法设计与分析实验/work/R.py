while True:
    n=int(input())
    if n==0:
        break
    # 战力不要溢出太多，最好是用“只能赢一点点，不能赢多了”那种
    a=sorted([int(_) for _ in input().split()])
    b=sorted([int(_) for _ in input().split()])
    pa,pb=0,0
    win=0
    for _ in range(n):
        if a[pa]>b[pb]:# 这匹能打赢，+1，让下一匹马打他家的下一个试试
            win+=1
            pa+=1
            pb+=1
        else:# 这匹打不赢，换更厉害的打
            pa+=1
    if win>n/2:
        print('YES')
    else:
        print('NO')