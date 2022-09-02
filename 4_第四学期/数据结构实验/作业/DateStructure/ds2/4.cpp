#include <cstdio>
const int maxn=500010;
int a[maxn],b[maxn];
long long num;
void Merge(int a[],int start,int mid,int end)
{
    int i=start,j=mid+1,k=start;
    while(i<=mid&&j<=end)
    {
        if(a[i]<=a[j])
        {
            b[k++]=a[i++];
        }
        else
        {
            num+=j-k;
            b[k++]=a[j++];
        }
    }
    while(i<=mid)
    {
        b[k++]=a[i++];
    }
    while(j<=end)
    {
        b[k++]=a[j++];
    }
    for(int i=start;i<=end;i++)
    {
        a[i]=b[i];
    }
}
void MergeSort(int a[],int start,int end)
{
    if(start<end)
    {
        int mid=(start+end)/2;
        MergeSort(a,start,mid);
        MergeSort(a,mid+1,end);
        Merge(a,start,mid,end);
    }
}
int main()
{
	int n;
    while(~scanf("%d",&n))
    {
    	if(n==0)
    		break;
        num=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        MergeSort(a,0,n-1);
        printf("%lld\n",num);
    }
    return 0;
}