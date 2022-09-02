# k转10
alphabet="0123456789ABCDEF"
def k2ten(s,k):
    sum=0
    for i,ch in enumerate(s[::-1]):
        sum+=alphabet.find(ch)*pow(k,i)
    print(sum)
# 10转k
def ten2k(x,k):
    if x>0:
        ten2k(x//k,k)
        print(alphabet[x%k],end='')

s=input()
k2ten(s,16)
n=int(input())
ten2k(n,16)
