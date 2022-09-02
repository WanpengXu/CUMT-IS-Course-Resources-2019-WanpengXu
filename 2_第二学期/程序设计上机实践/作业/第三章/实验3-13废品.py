print("A B C D")
for A in range(1,10):
    for B in range(1,10):
        for C in range(1,10):
            if A*B*C-pow(C,2)==0 :
                continue
            else :
                D=(A*B*C)/(A*B*C-pow(C,2))
                if D%1==0 and 0<D<10:
                    print(A,B,C,format(D,".0f"))
