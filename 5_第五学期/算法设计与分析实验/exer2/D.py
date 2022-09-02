n=int(input())
nums=[int(_) for _ in input().split()]
end,max_pos,step=0,0,0
for i in range(n-1):
    max_pos=max(max_pos,i+nums[i])
    if i==end:
        end=max_pos
        step+=1
print(step)