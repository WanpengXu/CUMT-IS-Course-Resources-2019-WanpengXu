#include <iostream>
#include <map>
#include <string>
#include <queue>
using namespace std;
string iswap(string str,int i){
    swap(str[i],str[i+1]);
    return str;
}
bool judge(string str){
    if(str.find("2012",0)==string::npos)
        return false;
    else
        return true;
}
int BFS(string str,map<string,int> &M,queue<string> &Q){
    string newStr;
    M.clear();
    while(!Q.empty())
        Q.pop();
    Q.push(str);
    M[str]=0;
    while(!Q.empty()){
        str=Q.front();
        Q.pop();
        for(unsigned i=0;i<str.length()-1;i++){
            newStr=iswap(str,i);
            if(M.find(newStr)==M.end()){
                M[newStr]=M[str]+1;
                if(judge(newStr)==true)
                    return M[newStr];
                else
                    Q.push(newStr);
            }
            else
                continue;
        }
    }
    return -1;
}
int main(){
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    map<string, int> M;
    queue<string> Q;
    int n;
    while(cin>>n){
        string str;
        cin>>str;
        if(judge(str)==true)
            cout<<"0"<<endl;
        else{
            cout<<BFS(str,M,Q)<<endl;
        }
    }
    return 0;
}