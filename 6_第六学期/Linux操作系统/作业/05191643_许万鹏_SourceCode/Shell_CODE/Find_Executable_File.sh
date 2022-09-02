#!/bin/bash

IFS=:  						# 内部字段分隔符（internal field separator）

if [ -n "$1" ]				# 尝试从参数获取输入
then
    dir=$1
    echo "正在查找$1/中的所有可执行文件..."
else
    dir=$PATH
    echo "正在查找PATH中的所有可执行文件..."
fi

for folder in $dir  		# 迭代dir中的所有folder
do
	echo "$folder:"  		# 打印当前迭代folder
	for file in $folder/*	# 迭代folder中的所有file
	do
		if [ -x $file ]		# 如果file有x权限
		then
			echo "  $file"  # 打印该可执行文件
		fi
	done
done
