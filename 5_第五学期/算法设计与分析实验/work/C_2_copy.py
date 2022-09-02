import re


def solve(s1, s2):
    l1 = re.split('\W+', s1)
    l2 = re.split('\W+', s2)
    if l1[-1] == '':
        l1.pop()
    if l2[-1] == '':
        l2.pop()

    def longestCommonSubsequence(text1,text2):
        m,n=len(text1),len(text2)
        if n==0 or m==0:
            return 'Blank!'
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return 'Length of longest match: {}'.format(dp[-1][-1])

    return longestCommonSubsequence(l1,l2)

counter = 1
while True:
    if counter % 2 == 0:
        s2 = input().strip()
        print('{:2}. {}'.format(counter//2,solve(s1, s2)))
    else:
        s1 = input().strip()
    counter += 1
