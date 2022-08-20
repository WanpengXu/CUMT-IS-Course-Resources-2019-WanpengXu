f=open("sy6-4.txt",'w')
def isprime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
if __name__=="__main__":
    #count=0
    for j in range(2,101):
        if isprime(j):
            #count+=1
            f.write(str(j)+" ")
            '''
            if count==5:
                count=0
                f.write("\n")
            '''
f.close()
