#include <iostream>
using namespace std;
int main(){
    int T;
    cin>>T;
    while(T--)
    {
        int n;
        cin>>n;
        int v=1,s=0;
        for(int i=0;i<n;i++){
            s=(s+v)%10000;
            v+=2;
        }
        cout<<s<<endl;
    }
    return 0;
}