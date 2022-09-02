#include <iostream>
#include <algorithm>
using namespace std;
int a[5];
int main(){
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int t;
    cin>>t;
    while(t--){
        for(int i=0;i<3;i++)
            cin>>a[i];
        sort(a,a+3);//左开右闭
        if(pow(a[0],2)+pow(a[1],2)==pow(a[2],2))
            cout<<"good"<<endl;
        else if(a[0]==a[1]||a[0]==a[2]||a[1]==a[2])
            cout<<"perfect"<<endl;
        else
            cout<<"just a triangle"<<endl;
    }
    return 0;
}