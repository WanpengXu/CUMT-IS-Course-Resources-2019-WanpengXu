#include <iostream>
using namespace std;
typedef long long ll;
const int maxn=1e5+100;
struct Object{
    ll w,v;
}o[maxn];
ll f[maxn];
int main()
{
    int N,W;
    cin>>N>>W;
    for(int i=1;i<=N;++i)
        cin>>o[i].w>>o[i].v;
    for(int i=1;i<=N;++i)
        for(int j=W;j>=o[i].w;--j)
            if(f[j-o[i].w]+o[i].v>f[j]) f[j]=f[j-o[i].w]+o[i].v;
    cout<<f[W];   
}