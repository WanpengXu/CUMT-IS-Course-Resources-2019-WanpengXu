while True:
    M,N=[int(_) for _ in input().split()]
    if M==0 and N==0:
        break
    homeworks=[]
    for _ in range(M):
        homework=[int(i) for i in input().split()]
        homework.append(homework[1]/homework[0])
        homeworks.append(homework)
    homeworks.sort(key=lambda x:x[2],reverse=True)
    values=0
    for homework in homeworks:
        if N>=homework[0]:
            values+=homework[1]
            N-=homework[0]
        else:
            values+=N*homework[2]
            break
    print("{:.2f}".format(values))