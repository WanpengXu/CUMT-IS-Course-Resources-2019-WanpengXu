def find(n,r):
    left=1
    right=n
    mid=(left+right)//2
    while left<right:
        mid=(left+right)//2
        if a[mid][1]==r:
            return mid
        elif a[mid][1]>r:
            right=mid-1
        else:
            left=mid+1
    return mid

while True:
    n,m=map(int,input().split())
    a=[]
    for _ in range(n):
        a.append([int(_) for _ in input().split()])
    a.sort(key=lambda x:(x[1],x[0]))
    a=[0]+a
    # print(a)
    for _ in range(m):
        l,r=map(int,input().split())
        ans=0
        k=find(n,r)
        # print('k=',k,sep='')
        for i in range(1,k+2):
            if l<=a[i][0] and a[i][1]<=r:
                ans+=1
                l=a[i][1]
        print(ans)
