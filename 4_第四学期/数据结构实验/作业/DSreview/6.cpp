#include <iostream>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int C;
    cin>>C;
    while(C--){
        int n,m;
        cin>>n>>m;
        if(n%(m+1)!=0)
            cout<<"first"<<endl;
        else
            cout<<"second"<<endl;
    }
    return 0;
}