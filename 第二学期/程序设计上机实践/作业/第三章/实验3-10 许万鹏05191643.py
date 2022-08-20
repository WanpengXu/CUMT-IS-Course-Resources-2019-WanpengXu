for i in range(1,1001):
    S=0
    for j in range(1,i):
        if i%j==0 :
            S+=j
    if S==i :
        print(i,end=",")
