#include <iostream>
#include <cmath>
using namespace std;
const int MAXN=50000+10;
double x[MAXN][2];
double cal(double xx,int n);
int main(){
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int Ca;
    cin>>Ca;
    int count=0;
    while(Ca--){
        count++;
        int n;
        cin>>n;
        for(int i=0;i<n;i++)
            cin>>x[i][0]>>x[i][1];
        double l=-1e6,r=1e6;
        while(l+1e-5<r){
            double lMid=l+(r-l)/3;
            double rMid=r-(r-l)/3;
            if(cal(lMid,n)<cal(rMid,n))
                r=rMid;
            else
                l=lMid;
        }
        cout<<"Case #"<<count<<": "<<(long long)(cal(l,n)+0.5)<<endl;
    }
    return 0;
}
double cal(double xx,int n){
    double sum=0;
    for(int i=0;i<n;i++)
        sum+=pow(fabs(x[i][0]-xx),3)*x[i][1];
    return sum;
}