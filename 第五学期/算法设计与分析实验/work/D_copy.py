def isometricLongestCommonSubsequence(text1,text2,len):
    dp=[[0]*(len+1) for _ in range(len+1)]
    for i in range(1,len+1):
        for j in range(1,len+1):
            if text1[i-1]==text2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]

def trans(input):
    trans=[0]*len(input)
    for i,event in enumerate(input):
        trans[int(event)-1]=i+1
    return trans

n=int(input())
input1=input().split()
trans1=trans(input1)
while True:
    input2=input().split()
    trans2=trans(input2)
    print(isometricLongestCommonSubsequence(trans1,trans2,n))