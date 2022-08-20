def common_divisor(m,n):
    r=m%n
    if r==0:
        return n
    else:
        return common_divisor(n,r) #函数前还要加return 否则相当于无返回值，else: 常数 
    
