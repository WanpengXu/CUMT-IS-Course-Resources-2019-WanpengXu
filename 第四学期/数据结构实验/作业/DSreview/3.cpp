#include <iostream>
using namespace std;
int main(){
    int n;
    while(cin>>n){
        long long ans=1;
        for(int i=1;i<=n;i++)
            ans=ans*(n+i)/i;
        ans/=n+1;
        cout<<ans<<endl;
    }
    return 0;
}