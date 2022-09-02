def dfs(x):# 第x位
    if x==len(ls)-1:# 如果全部固定完
        result.append(''.join(ls))# 添加结果
        return None# 返回空值
    st=set()# 创建空集合以去重及判断是否剪枝
    for i in range(x,len(ls)):# 对于第x位后的第i位
        if ls[i] in st:# 如果是重复字符
            continue# 跳过这个字符，即剪枝
        else:# 如果不是重复字符
            st.add(ls[i])# 加入欲移民第x位的字符黑名单
            ls[x],ls[i]=ls[i],ls[x]# 交换
            dfs(x+1)# 进入下一位
            ls[x],ls[i]=ls[i],ls[x]# 交换回去

str=input()[:-1]
ls=list(str)
result=[]
dfs(0)
result.sort()
print(' '.join(result))