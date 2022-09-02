a=[int(_) for _ in input().split()]
for i in a:
    flag=True
    for j in a:
        if i!=j and i%j==0:
            print(i)
            break