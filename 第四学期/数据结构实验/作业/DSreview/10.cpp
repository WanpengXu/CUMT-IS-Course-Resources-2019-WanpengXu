#include <iostream>
#include <algorithm>
//#include <functional>
using namespace std;
const int maxn=100000+10;
int a[maxn];
int compare (const void * a, const void * b){
  return ( *(int*)a - *(int*)b );
}//用qsort就必须写，此处为升序
int main(){
    int n;
    while(cin>>n){
        for(int i=0;i<n;i++)
            cin>>a[i];
        //sort(a,a+n,less<int>());
        qsort(a,n,sizeof(int),compare);
        for(int i=0;i<n;i++)
            cout<<a[i]<<' ';
        cout<<endl;
    }
    return 0;
}