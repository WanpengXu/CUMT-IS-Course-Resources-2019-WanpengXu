Scores={"Hanming":65,"Wanghai":97,"Mali":73,"Xulei":85,"Yangyi":92}
rank=reversed(sorted(Scores.items(),key=lambda d:d[1]))
for i in rank:
    print(i[0])
#有另解
