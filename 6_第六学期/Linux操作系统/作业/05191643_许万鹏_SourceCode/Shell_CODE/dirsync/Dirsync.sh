#!/bin/bash

usage() 											# 提示正确用法
{
    echo "Usage: $0 <mode:backup|sync> source_dir target_dir"
}

if [ $# -ne 3 ] ; then								# 如果输入参数不为3个，报错
    if [ $# -lt 3 ] ; then
        echo -n "Missing argument(s)! "
    elif [ $# -gt 3 ] ; then
        echo -n "Too many arguments! "
    fi
    usage
    exit 1
fi

if [ "$1" != "backup" -a "$1" != "sync" ] ; then	# 如果参数第一项不为 "backup" 或 "sync"，报错
    echo -n "Mode not recognized. "
    usage
    exit 1
fi

if [ ! -d "$2" ] ; then								# 输入源目录不存在，报错
    echo "$0: Source dir '$2': No such directory"
    exit 1
fi

mode=$1
src=$2; tgt=$3

rmExtraFiles()										# 接受两个参数：源文件夹、目标文件夹，递归删除目标文件夹中在源文件夹中不存在的文件
{
    for file in $2/* ; do							# 遍历目标文件夹中的所有文件
        if [ ! -e "${file/$2/$1}" ] ; then			# 如果文件在源文件夹中不存在，删除之
            rm -rf "$file"
        elif [ -d "$file" ] ; then					# 如果文件是目录，递归执行检查删除操作
            rmExtraFiles "${file/$2/$1}" "$file"
        fi
    done
}

sync()												# 同步功能
{
    [ ! -d "$2" ] && echo "Target directory '$2' does not exist. Creating target dir..." && mkdir -p "$2"   # 输入目标目录不存在，则创建新目录
    rmExtraFiles "$1" "$2"							# 首先移除目标文件夹中多余的文件
    cp -Trup "$1" "$2"								# 用源文件夹的文件更新目标文件夹（-u: 更新的文件才会被复制）
    cp -Trup "$2" "$1"								# 用目标文件夹的文件更新源文件夹
}

case $mode in
    backup)											# 备份功能
        echo "Backing up $src -> $tgt..."
        [ ! -d "$tgt" ] && echo "Target directory '$tgt' does not exist. Creating target dir..." && mkdir -p "$tgt"   # 输入目标目录不存在，则创建新目录
        # 将src目录递归地(-r)、保留属性地(-p)复制到tgt目录(-T: treat DEST as a normal file)，且当源文件更新/目标目录没有此文件时才复制(-u)，由此实现备份功能
        cp -Trup "$src" "$tgt" && echo "Backup from $src to $tgt completed!" || (echo "$0: Backup failed"; exit 1)
        ;;
    sync)											# 同步功能
        echo "Syncing $src <-> $tgt..."
        sync "$src" "$tgt" && echo "Sync $src and $tgt completed!" || (echo "$0: Sync failed"; exit 1)
        ;;
    *) 
        echo -n "$0: Mode error! "
        usage
        exit 1
        ;;
esac
exit 0