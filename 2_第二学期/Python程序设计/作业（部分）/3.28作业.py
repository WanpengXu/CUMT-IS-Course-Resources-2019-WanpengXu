print("一，二题答案")
print("""
BCCAAD

better
you
Physics
""")

print("三题答案整合")
print()

#3-1
aStr="Peace and love are good things"
print(aStr.find("love"))
bStr=aStr.replace("love","hope")
print(bStr)
print()

#3-2
names=["xiaoma","xiaowang","xiaoma","xiaoliu","xiaoma","xiaoliu"]
A=set(names)
B={}
for i in A:
    j=names.count(i)
    B[i]=j
print(B)
print()

#3-3
astr=input()
A,B=[],[]
for i in range(65,91):
    A.append(chr(i))
for j in range(97,123):
    B.append(chr(j))
A.extend(B)
for k in A:
    N=astr.count(k)
    if N!=0 :
        print(k,N)
print()

#3-4
alist=input().split(',')
flag=False
for i in alist:
    n=alist.count(i)
    if n!=1 :
        flag=True
print(flag)
print()
