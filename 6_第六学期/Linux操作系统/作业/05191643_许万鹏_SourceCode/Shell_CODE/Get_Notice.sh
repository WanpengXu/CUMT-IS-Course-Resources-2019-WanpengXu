#!/bin/bash

case $USER in
rich | barbara)
    echo "Welcome, $USER."
    echo "Please enjoy your work!";;
christine | tim)
    echo "Welcome, $USER."
    echo "Please finish your paper before the end of April!";;
xuwp)
    echo "Ohh, $USER! What are you doing in here loser? This is our turt!"
    echo "And guess what this is a no loser zone and you're not allowed!"
    echo "Now listen here $USER, root and rich are hosting the most epic party this weekend."
    echo "All the popular people are coming! But guess who's not coming?"
    echo "YOUU!!!"
    echo "Now run on /home/xuwp/ $USER before I make you do my homework!"
    echo "(root got him!)"
    echo "Get burnt!"
    echo "so Why haven't you started studying? Give you TEN seconds!"
    for ((i=1;i<=10;i++))
    do
        echo -e "$i..\c"
        sleep 1s
    done
    echo ""
    ;;
*)
    echo "Hello!";;
esac
