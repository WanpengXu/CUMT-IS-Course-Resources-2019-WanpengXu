n=int(input())
a=[]
for _ in range(n):
    a.append([int(_) for _ in input().split()])
a.sort(key=lambda x:(x[0],x[1]))
a=[0]+a
unwork_max=0
current_end_max=a[1][1]
work_max=a[1][1]-a[1][0]
current_work_max=a[1][1]-a[1][0]# 以第i个任务结束的连续工作时间
for i in range(2,n+1):
    if a[i][0]<=current_end_max:# 下一个任务来的时候上一个任务没结束
        if current_end_max<a[i][1]:
            current_work_max+=a[i][1]-current_end_max# 连续，叠加
    else:# 下一个任务来的时候上一个任务已经做完了
        unwork_max=max(unwork_max,a[i][0]-current_end_max)
        current_work_max=a[i][1]-a[i][0]# 间断，独立
    current_end_max=max(current_end_max,a[i][1])
    work_max=max(work_max,current_work_max)
print(work_max,unwork_max)