def count_num(str):
    dict={}
    list=str.split(' ')
    aset=set(list)
    for i in aset:
        dict[i]=list.count(i)#只能对集合计数
    dict1=sorted(dict.items(),key=lambda d:d[0])
    dict2=sorted(dict.items(),key=lambda d:d[1])
    print("Order of keys:")
    for k,v in dict1:
        print(k,v)
    print("Order of values:")
    for k,v in dict2:
        print(k,v)

if __name__=="__main__":
    S1="Python VB VFP C C++ Java Python Java Python C"
    count_num(S1)
