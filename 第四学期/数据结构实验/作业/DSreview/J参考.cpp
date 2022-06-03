#include<iostream>
#include<cmath>
typedef long long ll;
using namespace std;
double x[50005][2];
int n;
double cal(double xx){
    double sum=0;
    for(int i=0;i<n;i++){
        sum+=fabs(x[i][0]-xx)*fabs(x[i][0]-xx)*fabs(x[i][0]-xx)*x[i][1];
    }
    return sum;
}
int main(){
    int t;
    cin>>t;
    for(int w=1;w<=t;w++){
        cin>>n;
        for(int i=0;i<n;i++)
        cin>>x[i][0]>>x[i][1];
        double L=-1000000,r=1000000;
        while(L+0.00001<r){
            double Lmid=L+(r-L)/3;
            double rmid=r-(r-L)/3;
            if(cal(Lmid)<cal(rmid)) r=rmid;
            else L=Lmid;
        }
        cout<<"Case #"<<w<<": "<<(ll)(cal(L)+0.5)<<endl;
    }
    return 0;
}