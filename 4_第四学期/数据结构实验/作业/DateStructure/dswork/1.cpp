#include<iostream>
#include<algorithm> 
using namespace std;
int a[5];
int main()
{    
 int t;    
 while(cin>>t)   
  {       
    for(int i=1;i<=t;i++)       
     {            
      cin>>a[1]>>a[2]>>a[3];
      sort(a+1,a+4);            
      if(a[3]*a[3]==(a[1]*a[1]+a[2]*a[2]))
       cout<<"good"<<endl;            
      else if(a[1]==a[2]||a[1]==a[3]||a[2]==a[3]) 
       cout<<"perfect"<<endl;            
      else cout<<"just a triangle"<<endl;       
     }    
    }   
  return 0;
}
