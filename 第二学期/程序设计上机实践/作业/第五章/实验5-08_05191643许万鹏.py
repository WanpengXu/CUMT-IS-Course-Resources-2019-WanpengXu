def isSymmetrical(x):
    for k in range(0,4):
        for v in range(0,4):
            if x[k][v]!=x[v][k]:
                return False
    return True
        
def prime(x):
    #x=eval(x)
    if x==0 or x==1:
        return False
    else:
        for i in range(2,x):
            if x%i==0:
                return False
        return True

if __name__=="__main__":
    A=[[],[],[],[]]
    for j in range(0,4):
        A[j]=[eval(i) for i in input().split()]#可以不解析
    if isSymmetrical(A) is True:
        print("The matrix is symmetrical.")
    else:
        print("The matrix is not symmetrical.")
    icount=0
    for m in range(0,4):
        for n in range(0,4):
            if prime(A[m][n]) is True:
                icount+=1
    print("The matrix has {} prime number(s).".format(icount))
