n=int(input())
s=0
for i in range(1,n+1):
    k=0
    for j in range(1,i+1):
        k+=j
    s+=k
print(s)
