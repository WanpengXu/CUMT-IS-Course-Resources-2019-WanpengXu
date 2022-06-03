def fastpow(base,power,mod):
    result=1
    while power>0:
        if power&1:
            result=(result*base)%mod
        power>>=1
        base=(base*base)%mod
    return result

MOD=100000007# 用1e8+7会变成浮点数
while True:
    x=int(input())
    sum=0
    for i in range(1,x+1):
        sum+=fastpow(i,i,MOD)
    sum+=1
    sum%=MOD
    print(sum)