#include <iostream>
#include <string>
#include <map>
using namespace std;
const int maxn=2e4+10;//(80/(1+1))*500
void printdir(map<string,int>* msi,int link=0,int level=0);
int main(){
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    string dir,folder;
    int link=0;//CUMTOJ没越界（自动初始化？）
    map<string,int> msi[maxn];
    int N;
    cin>>N;
    while(N--){
        int now=0,pos=0;//当前目录，切片左端点
        int p=0;//CUMTOJ用unsinged会报错
        cin>>dir;
        while((p=dir.find('\\',p))!=dir.npos){
            folder=dir.substr(pos,p-pos);//substr(左端点，长度)
            if(!msi[now].count(folder))
                msi[now][folder]=++link;
            //跳转结构
            now=msi[now][folder];
            pos=++p;
        }
        folder=dir.substr(pos);//截到最后
        if(!msi[now].count(folder))
            msi[now][folder]=++link;
    }
    printdir(msi);
    return 0;
}
void printdir(map<string,int>* msi,int link,int level){
    //map默认有序
    for(map<string,int>::iterator it=msi[link].begin();it!=msi[link].end();it++){
        for(int i=0;i<level;i++)
            cout<<' ';
        cout<<it->first<<endl;//键
        printdir(msi,it->second,level+1);//值
    }
    return ;
}