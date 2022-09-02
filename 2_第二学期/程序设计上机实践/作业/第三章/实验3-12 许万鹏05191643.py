from random import randint
end="000"
while True :
    a=randint(0,9)
    b=randint(0,9)
    right=a+b
    print("{}+{}=?".format(a,b)) 
    print("请输入两个数的和，退出请输入000：",end="")
    x=input()
    if x==end :
        break
    elif eval(x)==right :
        print("运算正确！")
    else :
        print("{}+{}={} 继续努力！".format(a,b,right))
print("Process finished with exit code 0")
