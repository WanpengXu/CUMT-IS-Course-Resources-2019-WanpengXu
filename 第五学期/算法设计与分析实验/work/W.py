MOD=100000007
MAXN=25000+5

def qpow(base,power,mod):
    result=1
    while power>0:
        if power&1:
            result=(result*base)%mod
        base=(base*base)%mod
        power>>=1
    return result

sum=[0]
for i in range(1,MAXN+1):
    sum.append((sum[i-1]+qpow(i,i,MOD))%MOD)
# f=open("1.txt",'w')
# f.write('sum=['+','.join(map(str,sum))+']')
# f.close()
# 1.txt
while True:
    x=int(input())
    print((sum[x]+1)%MOD)