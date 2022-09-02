eps=1e-6
while True:
    T=int(input())
    if T==0:
        break
    CF=[int(_) for _ in input().split()]
    l=-1
    # r=float('inf')# 这个是真无穷大
    r=0x3F3F3F3F
    while abs(r-l)>eps:
        m=(l+r)/2
        NPV=0
        for i in range(0,T+1):
            NPV+=CF[i]*pow(1+m,T-i)# 对两侧乘(1+IRR)^T所得的通项
        # 单调递减函数
        if NPV>0:
            l=m
        else:
            r=m
    IRR=m
    print("{:.2f}".format(IRR))