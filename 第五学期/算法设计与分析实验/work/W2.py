# python的pow本身就是更优化的快速幂算法
MAXN=25000+5
MOD=100000007

sum=[0]
for i in range(1,MAXN+1):
    sum.append((sum[i-1]+pow(i,i,MOD))%MOD)
while True:
    x=int(input())
    print((sum[x]+1)%MOD)