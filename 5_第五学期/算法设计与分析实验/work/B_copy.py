book_types=[10,20,50,100]

def fill_table(table_size):
    books=[x//10 for x in book_types]
    table=[[0] * table_size for c in books]

    table[0]=[1]*table_size
    
    for i,v in enumerate(books):
        if i==0:
            continue
        for n in range(0,table_size):
            table[i][n]=table[i-1][n]+(table[i][n-v] if n>=v else 0)  
    return table

table = fill_table(1000//10+1)

cnt=int(input())
for o in range(cnt):
        n=int(input())
        if n%10!=0:
            print(0)
            continue
        v=table[len(book_types)-1][int(n//10)]
        print(v)