f=open("sy6-2.txt","r")
s=f.read(-1)
x=[eval(i) for i in s.split(",")]
xmax=max(x)
xmin=min(x)
print(xmax,xmin)
f.close()
