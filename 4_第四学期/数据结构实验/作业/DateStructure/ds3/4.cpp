#include <stdio.h>
#include <iostream>
#include <map>
#include <string>
#include <queue>
using namespace std;
map<string, int> M;//M[str]表示str经历的交换次数
queue<string> Q;//队列，用于bfs

string Swap(string str, int i)
{//将字符串i位与i+1位交换
    string newStr=str;
    char tmp=newStr[i];
    newStr[i]=newStr[i+1];
    newStr[i+1]=tmp;
    return newStr;
}

bool Judge(string str)
{//判断字符串中是否含有"2012"
    if(str.find("2012", 0)==string::npos) return false;
    else return true;
}

int BFS(string str)
{//广度优先搜索
    string newStr;
    M.clear();//清空map
    while(!Q.empty()) Q.pop();//清空队列
    Q.push(str);//初始字符串作为起点放入队列
    M[str]=0;//初始字符串经历的交换次数是0
    while(!Q.empty())
    {
        str=Q.front();
        Q.pop();//取出队首，存入str
        for(unsigned i=0; i<str.size()-1; i++)//尝试进行一次交换
        {
            newStr=Swap(str, i);//新字符串由str交换i位和i+1位得到
            if(M.find(newStr)==M.end())//如果这个字符串没出现过
            {
                M[newStr]=M[str]+1;//现在出现过了，且交换次数比他爹多1
                if(Judge(newStr)==true) return M[newStr];//符合要求，收工
                else Q.push(newStr);//不合要求，那继续bfs，把它加入队列
            }
            else continue;//出现过的字符串，不用进行处理
        }
    }
    return -1;//遍历完成，没发现符合要求的字符串，返回-1
}

int main()
{
    int n;
    string str;
    while(scanf("%d", &n)!=EOF)
    {
        cin>>str;//读取字符串(前面读取n好像没啥用)
        if(Judge(str)==true) printf("0\n");//一开始就符合要求的话
        else//初始字符串不符合要求，那就bfs
        {
            int ans=BFS(str);
            printf("%d\n", ans);
        }
    }
    return 0;//大功告成
}