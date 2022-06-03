def check(x,y):# 界内检查
    if 1<=x<=n and 1<=y<=m:
        return True
    else:
        return False

def dfs(x,y):# x行y列
    vis[x][y]=True
    # print('走到了',x,y)
    if mz[x][y]=='T':
        flag[0]=True
        return None
    for dir in dirs:
        xx=x+dir[0]
        yy=y+dir[1]
        # print("准备走",xx,yy)
        if check(xx,yy) and \
            (mz[xx][yy] in ['.','T']) and \
            vis[xx][yy]==False and \
            flag[0]==False:
            # print('实际走',xx,yy)
            dfs(xx,yy)

# dirs=[(-1,0),(1,0),(0,-1),(0,1)]# 上下左右
dirs=[(0,-1),(-1,0),(0,1),(1,0)]# 左上右下
n,m=map(int,input().split())# n行m列
mz=[' '*(m+1)]
vis=[[False]*(m+1) for _ in range(n+1)]
for i in range(n):
    mz_row=' '+input()
    mz.append(mz_row)

# for i in mz:
#     print(i)

flag=[False]
for i in range(1,n+1):
    for j in range(1,m+1):
        if mz[i][j]=='S':
            dfs(i,j)
if flag[0]:
    print('YES')
else:
    print('NO')