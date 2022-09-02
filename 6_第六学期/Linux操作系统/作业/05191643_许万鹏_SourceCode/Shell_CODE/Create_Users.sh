#!/bin/bash

if [ -n "$1" ]						# 尝试从参数获取输入
then
    input=$1
else
    input="users.csv"
fi
IFS=','  							# 将IFS设置为csv文件的分隔符,

echo "$input文件中的内容为："
cat $input | while read line
do
    echo $line
done
echo

echo "开始添加用户..."
while read -r userid name  			#  从输入中读取一行
do
    echo "adding $userid"
    useradd -c "$name" -m $userid	# 添加该user
done < "$input"  					# 在while尾部使用重定向符<将输入重定向至input
echo "用户添加完毕！"
