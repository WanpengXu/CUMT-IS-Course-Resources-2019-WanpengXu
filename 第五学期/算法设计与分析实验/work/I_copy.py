while True:
    n=int(input())
    if n==0:
        break
    exons=[]
    exons_ans=[]
    for counter in range(1,n+1):
        exon=[counter]
        exon.extend([int(_) for _ in input().split()])
        exons.append(exon)
    # exons.sort(key=lambda x:x[2])
    # 按结束位置贪心，结束位置越早，后面能加入的串就越多
    # endpos=0
    # for exon in exons:
    #     if endpos<exon[1]:
    #         exons_ans.append(exon[0])
    #         endpos=exon[2]
    # print(' '.join(map(str,exons_ans)))

    exons.sort(key=lambda x:x[1],reverse=True)
    # 按开始位置贪心，开始位置越晚，前面能加入的串就越多
    startpos=float('Inf')
    for exon in exons:
        if startpos>exon[2]:
            exons_ans.append(exon[0])
            startpos=exon[1]
    print(' '.join(map(str,exons_ans[::-1])))