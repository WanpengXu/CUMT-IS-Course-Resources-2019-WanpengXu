print('已知向量α（x1I,y1J,z1K），向量β（x2I,y2J,z2K），求α×β')
xa=eval(input('向量α（x1I,y1J,z1K）的x1值为:'))
ya=eval(input('向量α（x1I,y1J,z1K）的y1值为:'))
za=eval(input('向量α（x1I,y1J,z1K）的z1值为:'))
xb=eval(input('向量β（x2I,y2J,z2K）的x2值为:'))
yb=eval(input('向量β（x2I,y2J,z2K）的y2值为:'))
zb=eval(input('向量β（x2I,y2J,z2K）的z2值为:'))
i=ya*zb-za*yb
j=za*xb-xa*zb
k=xa*yb-ya*xb
print("结果为(",i,',',j,',',k,end=')')
