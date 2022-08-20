from random import randint
A,B,C=[],[],[]
for i in range(65,91):
    A.append(chr(i))
for j in range(97,123):
    B.append(chr(j))
for k in range(48,58):
    C.append(chr(k))
A.extend(B)
A.extend(C)
for i in range(1,11):
    keywords=[]
    for j in range(1,9):
        k=randint(0,61)
        keywords.extend(A[k])
    strkeywords=''.join(keywords)
    print(strkeywords)
