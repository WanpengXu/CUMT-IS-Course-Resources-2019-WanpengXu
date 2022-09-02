#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    string s;
    while(cin>>s){
        string a[s.size()];
        for(int i=0;i<s.size();i++)
            a[i]=s.substr(i,s.size()-i);
        sort(a,a+s.size());
        for(int i=0;i<s.size();i++)
            cout<<a[i]<<endl;
    }
    return 0;
}