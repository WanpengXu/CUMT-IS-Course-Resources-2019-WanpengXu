#include <iostream>
using namespace std;
int main()
{
	int T,i,n;
	cin>>T;
	while(T--){
		cin>>n;
		int w=1,s=0;
		for(i=1;i<=n;i++){
			w=(2*i-1)%10000;
			s=(s+w)%10000;
        }
		cout<<s<<endl;
	}
	return 0;
}