# TLE33%

def dfs(track):
    if len(track)==len(str) and\
    track not in res:
        res.append(track)
        return None
    for j in range(len(str)):
        if vis[j]:
            continue
        vis[j]=1
        dfs(track+str[j])
        vis[j]=0

str=input()[:-1]
vis=[0]*len(str)
res=[]
dfs('')
res.sort()
print(' '.join(res))