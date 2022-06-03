def check(x,y):
    if 1<=x<=r and 1<=y<=c:
        return True
    else:
        return False

def dfs(x,y):
    if vis[x][y]:
        return None
    vis[x][y]=True
    for dir in dirs:
        xx=x+dir[0]
        yy=y+dir[1]
        if check(xx,yy) and m[x][y]>m[xx][yy]:
            dfs(xx,yy)
            dp[x][y]=max(dp[x][y],dp[xx][yy]+1)

dirs=[(0,1),(0,-1),(-1,0),(1,0)]

r,c=map(int,input().split())
m=[[0]*(c+1)]
dp=[[1]*(c+1) for _ in range(r+1)]
vis=[[False]*(c+1) for _ in range(r+1)]
for i in range(r):
    m_row=[0]+[int(_) for _ in input().split()]
    m.append(m_row)
ans=0
for i in range(1,r+1):
    for j in range(1,c+1):
        dfs(i,j)
        ans=max(ans,dp[i][j])
print(ans)