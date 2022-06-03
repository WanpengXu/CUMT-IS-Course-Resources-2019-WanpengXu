#include<stdio.h>
void quicksort(int left,int right);
int a[100010];
int main()
{
	int n,i;
	while(scanf("%d",&n)!=EOF)
	{
		for(i=1;i<=n;i++)
			scanf("%d",&a[i]);
		quicksort(1,n);
		for(i=1;i<=n;i++)
			printf("%d ",a[i]);
		printf("\n");
	}
	return 0;
}
void quicksort(int left,int right)//快速排序核心代码
{
	int i,j,t,x;
	if(left>right)
		return;
	
	i=left;
	j=right;
	x=a[left];
	
	while(i!=j)
	{
		while(a[j]>=x&&i<j)//如果基准右边比基准大直接查找下一个位置，直到找到比基准小的值
			j--;
		while(a[i]<=x&&i<j)//如果基准左边比基准小直接查找下一个位置，直到找到比基准大的值
	                i++;
		if(i<j)//交换
		{
			t=a[i];
			a[i]=a[j];
			a[j]=t;
		}
	}
        //基准与相同位置的值互换
        a[left]=a[i];
	a[i]=x;
	
        //递归分别排基准左边和右边的子序列
	quicksort(left,i-1);
	quicksort(i+1,right);
	
	return;
}