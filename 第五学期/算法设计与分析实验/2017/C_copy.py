def check(x,y):# 界内检查
    if 1<=x and x<=n and 1<=y and y<=m:
        return True
    else:
        return False

def dfs(x,y):
    global flag
    vis[x][y]=True
    # print('走到了',x,y)
    if mz[x][y]=='t':
        flag=True
        return None
    for dir in dirs:
        xx=x+dir[1]
        yy=y+dir[0]
        # print("准备走",xx,yy)
        if check(xx,yy) and (mz[xx][yy] in ['.','t']) and vis[xx][yy]==False and flag==False:
            # print('实际走',xx,yy)
            dfs(xx,yy)

dirs=[(0,-1),(0,1),(-1,0),(1,0)]
T=int(input())
while True:
    if T==0:
        break
    T-=1
    n,m=map(int,input().split())
    mz=[' '*(m+1)]
    vis=[[False]*(m+1) for _ in range(n+1)]
    for i in range(n):
        mz_row=' '+input()
        mz.append(mz_row)

    # for i in mz:
    #     print(i)

    flag=False
    for i in range(1,n+1):
        for j in range(1,m+1):
            if mz[i][j]=='s':
                dfs(i,j)
                break
    if flag:
        print('YES')
    else:
        print('NO')