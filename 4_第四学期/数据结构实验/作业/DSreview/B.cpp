#include <iostream>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int T;
    cin>>T;
    while(T--){
        int ASCII;
        cin>>ASCII;
        cout<<char(ASCII);
    }
    return 0;
}