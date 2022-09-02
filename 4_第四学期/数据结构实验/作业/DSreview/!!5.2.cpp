#include<iostream>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int m,n;
    while(cin>>m>>n&&m&&n){
        if(n>m)
            swap(n,m);
        bool flag=true;
        while(m%n!=0&&m/n==1){
            m-=n;
            if(n>m)
                swap(n,m);
            flag=!flag;
        }
        if(flag)
            cout<<"xiaoming wins"<<endl;
        else
            cout<<"xiaohong wins"<<endl;
    }
    return 0;
}