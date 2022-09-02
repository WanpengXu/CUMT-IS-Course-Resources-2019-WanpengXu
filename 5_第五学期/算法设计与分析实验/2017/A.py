alphabet="0123456789ABCDEF"
def ten2k(x,k):
    if x>0:
        ten2k(x//k,k)# 除k
        print(alphabet[x%k],end='')# 倒取余

n=int(input())

print(("{}".format(n)).upper())
ten2k(n,10)
print()

print(("{:b}".format(n)).upper())
ten2k(n,2)
print()

print(("{:o}".format(n)).upper())
ten2k(n,8)
print()

print(("{:x}".format(n)).upper())
ten2k(n,16)
print()

ten2k(n,7)
print()