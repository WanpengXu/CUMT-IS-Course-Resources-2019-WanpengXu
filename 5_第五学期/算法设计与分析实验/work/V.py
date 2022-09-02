def backtrack(s,path):
    if len(s)==0:
        res.append(path)
        return None
    vis=set()
    for i in range(len(s)):
        if s[i] in vis:
            continue
        vis.add(s[i])
        backtrack(s[:i]+s[i+1:],path+s[i])

str=input()[:-1]
res=[]
backtrack(str,'')
# res.sort()
# for i in res:
#     print(i,end=' ')
print(' '.join(sorted(res))) #没有循环会快一点