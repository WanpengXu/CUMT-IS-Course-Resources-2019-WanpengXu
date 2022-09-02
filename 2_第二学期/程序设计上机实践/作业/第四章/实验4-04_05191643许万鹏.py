scores=[0,1,2,3,4,5,6,7,8,9]
scores.sort()
scores.pop(0)
scores.pop()
'''
total=0
for i in scores:
    total+=i
'''
total=sum(scores)
average=total/8
print(average)
