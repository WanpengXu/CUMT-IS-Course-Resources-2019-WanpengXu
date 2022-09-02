#include <iostream>
using namespace std;
const int maxn=500000+50;
typedef long long LL;
int a[maxn],b[maxn];
void merge(int* a,int start,int mid,int end,LL &num);
void mergeSort(int* a,int start,int end,LL &num);
int main(){
    //相关知识点：归并排序、逆序数组
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int n;
    while(cin>>n&&n!=0){
        LL N=0;
        for(int i=0;i<n;i++)
            cin>>a[i];
        mergeSort(a,0,n-1,N);
        cout<<N<<endl;
    }
    return 0;
}
void merge(int* a,int start,int mid,int end,LL &num){
    int i=start,j=mid+1,k=start;
    while(i<=mid&&j<=end){
        if(a[i]<=a[j])
            b[k++]=a[i++];
        else{
            num+=j-k;
            //cout<<j-k<<endl;
            b[k++]=a[j++];
        }
    }
    while(i<=mid)
        b[k++]=a[i++];
    while(j<=end)
        b[k++]=a[j++];
    for(int i=start;i<=end;i++)
        a[i]=b[i];
}
void mergeSort(int* a,int start,int end,LL &num){
    if(start<end){
        int mid=(start+end)/2;
        mergeSort(a,start,mid,num);
        mergeSort(a,mid+1,end,num);
        merge(a,start,mid,end,num);
    }
}