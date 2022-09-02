while True:
    M,N=map(int,input().split())
    if M==0 and N==0:
        break
    works=[]
    for _ in range(M):
        work=[int(_) for _ in input().split()]
        work.append(work[1]/work[0])
        works.append(work)
    works.sort(key=lambda x:x[2],reverse=True)
    values=0
    for work in works:
        if N>=work[0]:
            values+=work[1]
            N-=work[0]
        else:
            values+=N*work[2]
            N-=N
            break
    print("{:.2f}".format(values))