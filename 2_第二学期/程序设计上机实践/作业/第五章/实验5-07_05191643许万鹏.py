def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

if __name__=="__main__":
    n=int(input())
    print(fib(n))
