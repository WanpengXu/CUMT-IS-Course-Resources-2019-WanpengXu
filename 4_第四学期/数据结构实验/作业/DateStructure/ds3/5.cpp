#include<iostream>
using namespace std;
int a[1005];
int main(){
    int  n;
    cin>>n;
    for(int i=0;i<n;i++) cin>>a[i];
    int low,high,mid;
    for(int i=1;i<n;i++){
        int low=0;high=i-1;
        int k=a[i];
        while(low<=high){
            mid=(low+high)>>1;
            if(a[i]<a[mid]) high=mid-1;
            else
            low =mid+1;
        }
        for(int j=i;j>=low+1;j--) a[j]=a[j-1];
        a[low]=k;
    }
    for(int i=0;i<n;i++) cout<<a[i]<<" ";
    cout<<endl;
    return 0;
}