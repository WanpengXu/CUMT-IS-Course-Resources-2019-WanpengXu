#include <iostream>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int a,b;
    while(cin>>a>>b&&!(a==0&&b==0)){
        bool flag=true;
        if(a==b)
            cout<<"xiaoming wins"<<endl;
        else{
            while(a!=b){
                if(a<b)
                    swap(a,b);
                flag=!flag;
                if(a/b!=1)
                    break;
                a%=b;
            }
        if(flag)
            cout<<"xiaohong wins"<<endl;
        else
            cout<<"xiaoming wins"<<endl;
        }
    }
    return 0;
}