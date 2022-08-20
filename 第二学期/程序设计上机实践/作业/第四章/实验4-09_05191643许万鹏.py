dic={"Administrator":"123456","Guest":"098765"}
j=3
for i in range(0,3):
    User=input("User:")
    password=input("password:")
    enter={User:password}
    if set(enter.items())<=set(dic.items()):#或采用集合方法A.issubset(B)[A是否是B的子集，返回布尔值]
        print("Welcome!")
        break
    else:
        j-=1
        print("您还有{}次输入机会".format(j))
else:
    print("无法登陆，即将自动关闭")
