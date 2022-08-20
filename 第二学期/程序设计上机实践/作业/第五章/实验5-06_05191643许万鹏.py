def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

if __name__=="__main__":
    icount=0
    for j in range(4,1002,2):
        for k in range(2,j):
            if prime(k) and prime(j-k):
                print("{}={}+{}".format(j,k,j-k),end=',')
                icount+=1
                if icount==6:
                    print()
                    icount=0
                    break
                break
        
