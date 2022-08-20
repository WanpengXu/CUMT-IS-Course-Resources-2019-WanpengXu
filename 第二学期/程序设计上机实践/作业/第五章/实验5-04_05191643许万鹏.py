dic={}
def add_dic(word,translation):
    dic[word]=translation
def search_dic(word):
    return dic[word]
while True:
    print("choose 1-input,2-look for,3-exit")
    choose=eval(input())
    if choose==1:
        a=input("please input an English word:")
        b=input("please input the Chinese meaning:")
        add_dic(a,b)
    elif choose==2:
        c=input("please input the word you want to look for:")
        print(c,search_dic(c))
    elif choose==3:
        break
