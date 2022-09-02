vote={4,7,8,1,2,2,6,2,2,1,6,8,7,4,5,5,5,8,5,5,4,2,2,6,4}
#1)
vote1=set(vote)
print(vote)
#2)
list1={1,2,3,4}
print(list1&vote1)
#3)
list2={5,6,7,8}
temp=list2-vote
if temp==set():#set()为空集合 {}不是
    print("不存在没有获得选票的候选人")
else :
    print(temp)
#4)
list3={eval(input())}
if list3<vote :
    print("获得了选票")
else :
    print("未获得选票")
