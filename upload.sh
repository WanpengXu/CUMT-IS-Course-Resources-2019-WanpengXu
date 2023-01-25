#！/bin/sh 

git add .
git commit -m "5th commit - Seventh Semester and README.md"
git remote set-url origin https://github.com/WanpengXu/CUMT-IS-Course-Resources-2019-WanpengXu.git
git config --global http.postBuffer 524288000
git pull --rebase origin main
git push -u origin main
exec /bin/bash