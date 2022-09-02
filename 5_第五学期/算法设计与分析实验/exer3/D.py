N=int(input())
a=[0]
cnt=[0]*(3+1)
for _ in range(1,N+1):
    x=int(input())
    a.append(x)
    cnt[x]+=1
sum1,sum2,sum3=0,0,0
for i in range(1,cnt[1]+1):
    if a[i]!=1:
        sum1+=1
for i in range(cnt[1]+1,cnt[1]+cnt[2]+1):
    if a[i]==3:
        sum2+=1
for i in range(cnt[1]+cnt[2]+1,N+1):
    if a[i]==2:
        sum3+=1
print(sum1+max(sum2,sum3))