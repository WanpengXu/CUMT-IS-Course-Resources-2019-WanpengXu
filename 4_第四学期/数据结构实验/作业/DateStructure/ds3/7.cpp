#include<iostream>
#include<cstdio>
#include<algorithm>
#include<queue> 
#include<string>
#include<map>
  
using namespace std; 
  
typedef map<string,int> msi;
const int N=2e4;
msi ms[N];
  
int tot;
  
void print(int m,int s){
    for(msi::iterator it=ms[m].begin();it!=ms[m].end();it++){
        for(int i=0;i<s;i++)
        putchar(' ');
        cout<<it->first<<endl;
        print(it->second,s+1);
    }
}
  
string t,s;
  
int main(){
    int n;
    scanf("%d",&n);
    while(n--){
        int now=0,pos=0,p=0;
        cin>>t;
        while((p=t.find('\\',p))!=-1){
            s=t.substr(pos,p-pos);
            if(!ms[now].count(s))ms[now][s]=++tot;
            now=ms[now][s];
            pos=++p;
        }
        s=t.substr(pos);
        if(!ms[now].count(s))ms[now][s]=++tot;
    }
    print(0,0);
}
