#!/bin/bash

eps=0.00000001  										# 保留6位小数，精度取6+2=8位，故为1e-8

# read -p "please input a num: " x						# 从IO读取输入
x=$1													# 从参数读取输入

l=-100; r=100
until delta=`echo $l $r | awk '{printf "%.8f",$2-$1}'`  # 计算区间长度delta
    [ `echo $delta $eps | awk '{printf ($1<=$2)?"true":"false"}'` == "true" ]  # 直到满足精度eps为止
do
    mid=`echo $l $r | awk '{printf "%.8f",($1+$2)/2}'`	# 计算区间中点mid
    val=`echo $mid | awk '{printf "%.8f",$1*$1*$1}'`	# 计算当前mid的三次方
    if [ `echo $val $x | awk '{printf $1>=$2}'` -eq 1 ]	# 如果mid大了
	then
		r=$mid											# 右端点向左缩
	else												# 如果mid小了
		l=$mid											#左端点向右缩
	fi
done

printf "%.6f\n" $l
