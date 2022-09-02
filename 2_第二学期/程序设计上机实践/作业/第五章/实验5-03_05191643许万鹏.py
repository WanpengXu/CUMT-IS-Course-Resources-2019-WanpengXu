def rank(x):
    list1=list(x)
    list2=reversed(sorted(list1))
    rankstr=''.join(list2)
    return rankstr

if __name__=="__main__":
    m=input()
    result=rank(m)
    print(result)
