MOD=1000000007
fib=[1,1]
for i in range(2,100+1):
    fib.append((fib[i-1]+fib[i-2])%MOD)

while True:
    n=int(input())
    print(fib[n])