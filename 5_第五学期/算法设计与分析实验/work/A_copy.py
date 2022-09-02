MAXN=100+5
dp=[[0]*MAXN for _ in range(MAXN)]
s=[[0]*MAXN for _ in range(MAXN)]

def print_path(i,j):
    if i>j:
        return None
    elif i==j:# 断到最后剩下的肯定是单个括号
        if str[i] in ('(',')'):
            print('()',end='')
        else:
            print('[]',end='')
    else:
        if s[i][j]==-1:
            print(str[i],end='')
            print_path(i+1,j-1)
            print(str[j],end='')
        else:
            print_path(i,s[i][j])
            print_path(s[i][j]+1,j)

str=' '+input()
length=len(str[1:])
for i in range(1,length+1):
    dp[i][i]=1
for l in range(2,length+1):# 子串的长度递增
    for i in range(1,length-l+1+1):# 子串的起始下标
        j=i+l-1# 子串的结束下标=子串的起始下标+子串的长度-1
        if \
        str[i]=='(' and str[j]==')' or \
        str[i]=='[' and str[j]==']': # 如果匹配上了
            dp[i][j]=dp[i+1][j-1]# 记录“左右指针ij往里缩一位后的子串”所需的加括号数量
            s[i][j]=-1# 记录子串未断开
        else:# 如果没匹配上
            dp[i][j]=float('INF')# 打擂法，设置加括号数量为无穷大，后面找最小
        for k in range(i,j):# 将不能匹配的子串按断开点（决策点）k分为两段，找使这两子串加括号数量之和最小的最优k
            if dp[i][k]+dp[k+1][j]<dp[i][j]:
                dp[i][j]=dp[i][k]+dp[k+1][j]
                s[i][j]=k# 记录最优断开点
print_path(1,length)
print()