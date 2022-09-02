#include <iostream>
using namespace std;
int a[1005]={};
void BInsertSort(int *a,int n);
int main(){
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>a[i];
    BInsertSort(a,n);
    for(int i=0;i<n;i++)
        cout<<a[i]<<" ";
    cout<<endl;
    return 0;
}
void BInsertSort(int *a,int n){
    int low,high,mid;
    for(int i=1;i<n;i++){
        low=0;
        high=i-1;
        int t=a[i];
        while(low<=high){
            mid=(low+high)/2;
            if(a[i]<a[mid])
                high=mid-1;
            else
                low=mid+1;
        }
        for(int j=i-1;j>=low;j--)
            a[j+1]=a[j];
        a[low]=t;
    }
}