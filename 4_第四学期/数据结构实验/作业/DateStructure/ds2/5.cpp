#include<iostream>
using namespace std;
int main()
{
	int a,b;
	int c,d;
	while(cin>>a,cin>>b,a!=0||b!=0)
	{   d=1;
		if(a==b) 
		{
			cout<<"xiaoming wins"<<endl;
		}
		else
		{
		   while(a!=b)
			{
			if(a<b)
			{
				c=a;
				a=b;
				b=c;
			}
			d++;
			if(a/b!=1)
			{
					break;
			} 
			
				a=a%b;
			}
		if(d%2==1)
			cout<<"xiaohong wins"<<endl;
		else
			cout<<"xiaoming wins"<<endl;
		}
 
	}
	return 0;
}