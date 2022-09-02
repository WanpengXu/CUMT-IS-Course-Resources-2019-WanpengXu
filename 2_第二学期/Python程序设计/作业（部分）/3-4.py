n=eval(input("请输入项数"))
N=n//2
if n%2==0 :
    S1=0
    for i in range(1,1+(N-1)*4+1,4):
        S1=S1+i
    S2=0
    for j in range(-3+(N-1)*(-4),-2,4):
        S2=S2+j
else :
    S1=0
    for i in range(1,1+(N+1-1)*4+1,4):
        S1=S1+i
    S2=0
    for j in range(-3+(N-1)*(-4),-2,4):
        S2=S2+j
S=S1+S2
print("S=",S,sep="")
















'''
S1=0
for i in range(1,1+(N-1)*4+1,4):
    S1=S1+i
print(S1)
S2=0
for j in range(-3+(N-1)*(-4),-2,4):
    S2=S2+j
print(S2)
S=S1+S2
print("S=",S)
'''
