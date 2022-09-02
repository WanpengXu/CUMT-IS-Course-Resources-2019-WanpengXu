#!/bin/bash

newerFile=`find $1 -newer $2`
echo "\$1: $1"
echo "\$2: $2"
echo "newerFile: $newerFile"

if [ "$newerFile" == "$1" ] ; then
    echo "$1 is newer than $2"
else
    echo "$2 is newer than $1"
fi