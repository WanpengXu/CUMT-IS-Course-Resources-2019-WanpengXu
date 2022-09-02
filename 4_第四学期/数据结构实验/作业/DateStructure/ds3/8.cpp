#include<cmath>
#include<iostream>
using namespace std;
typedef long long ll;
const int MAXN = 50010;
const int inf = 0x3fffffff;
const double EPS = 1e-6;
int t,n;
double x[MAXN],w[MAXN];    
 
double chu(double start)       
{
 double sum=0;
 for(int i=0;i<n;i++)
 {
     double d=x[i]-start;
     if(d<0) d=-d;
     sum+=d*d*d*w[i];
 }
 return sum;
}
int main()
{
 cin>>t;
double l,r;
 for(int num=1;num<=t;num++)
 {
  cin>>n;
  l=inf,r=-inf;
  for(int i=0;i<n;i++)
  {
     cin>>x[i]>>w[i];
     if (x[i] > r)
        r= x[i];
    if (x[i] <l)
        l = x[i];
  }
  while(r-l>EPS)            
  {
     double m1=(l+r)/2.0;
     double m2=(m1+r)/2.0;
     if(chu(m1)>chu(m2)) l=m1;
     else r=m2;
  }
 cout<<"Case #"<<num<<": "<< ll(chu(l)+0.5)<<endl;
 }
 return 0;
}
