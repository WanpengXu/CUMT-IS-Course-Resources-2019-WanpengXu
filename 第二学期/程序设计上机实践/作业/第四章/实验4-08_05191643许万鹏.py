months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
days=[31,28,31,30,31,30,31,31,30,31,30,31]
monthdays=dict(zip(months,days))
print(monthdays.keys())#输出
print(monthdays.values())#输出
print(monthdays.items())#输出
print(monthdays.get("May"))#获取
monthdays.update({"Feb":29})#修改
d={"a1":35,"a2":35}#创建
monthdays.update(d)#更新
monthdays.pop("a1")#删除
