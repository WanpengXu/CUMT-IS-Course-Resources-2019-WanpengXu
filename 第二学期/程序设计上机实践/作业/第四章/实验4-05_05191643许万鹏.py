scores=[50,60,70,80,90,100]
sum1,sum2=0,0
n1,n2=0,0
for i in scores:
    if i<60:
        sum1+=i
        n1+=1
    elif i>=90:
        sum2+=i
        n2+=1
average1=sum1/n1
average2=sum2/n2
print(average1,average2)
