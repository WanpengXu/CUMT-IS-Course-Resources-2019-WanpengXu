#include <iostream>
using namespace std;
int a[1005]={};
void bInsertSort(int L[],int n){
    int low,high,mid;
    for(int i=1;i<n;i++){
        low=0;
        high=i-1;
        int temp=L[i];
        while(low<=high){
            mid=(low+high)/2;
            if(temp<L[mid])
                high=mid-1;
            else
                low=mid+1;
        }
        for(int j=i-1;j>=low;j--)
            L[j+1]=L[j];
        L[low]=temp;
    }
}
int main(){
    int N;
    cin>>N;
    for(int i=0;i<N;i++)
        cin>>a[i];
    bInsertSort(a,N);
    for(int i=0;i<N;i++)
        cout<<a[i]<<' ';
    cout<<endl;
    return 0;
}