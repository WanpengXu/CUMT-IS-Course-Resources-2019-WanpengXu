#include <iostream>
#include <string>
#include <map>
using namespace std;
const int maxn=2e4;
void printdir(map<string,int>* msi,int m,int s);
int main(){
    string t,s;
    int tot;
    map<string,int> msi[maxn];
    int N;
    cin>>N;
    while(N--){
        int now=0,pos=0,p=0;
        cin>>t;
        while((p=t.find('\\',p))!=-1){
            s=t.substr(pos,p-pos);
            if(!msi[now].count(s))
                msi[now][s]=++tot;
            now=msi[now][s];
            pos=++p;
        }
        s=t.substr(pos);
        if(!msi[now].count(s))
            msi[now][s]=++tot;
    }
    printdir(msi,0,0);
    return 0;
}
void printdir(map<string,int>* msi,int m,int s){
    for(map<string,int>::iterator it=msi[m].begin();it!=msi[m].end();it++){
        for(int i=0;i<s;i++)
            cout<<' ';
        cout<<it->first<<endl;
        printdir(msi,it->second,s+1);
    }
}