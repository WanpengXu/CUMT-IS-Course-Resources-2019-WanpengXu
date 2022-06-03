#include <iostream>
using namespace std;
int main(){
    int n;
    while(cin>>n){
        long long ans=1;
        for(double i=1;i<=n;i++)
            ans*=(n+i)/i;
        cout<<ans/(n+1)<<endl;
    }
    return 0;
}