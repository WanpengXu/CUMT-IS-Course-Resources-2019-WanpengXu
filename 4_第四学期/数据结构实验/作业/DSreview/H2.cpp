#include <iostream>
using namespace std;
const int INF=INT32_MAX;
class Graph{
public:
    int n;
    int G[55][55];
    Graph(int num){
        n=num;
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++){
                cin>>G[i][j];
                if(i!=j&&G[i][j]==0)
                    G[i][j]=INF;
            }
    }
    int prim(){
        int lowcost[55];
        int mst[55];
        int sum=0;
        for(int i=1;i<=n;i++){
            lowcost[i]=G[1][i];
            mst[i]=0;
        }
        lowcost[1]=0;
        mst[1]=1;//1是加入
        //cout<<1;
        for(int i=1;i<n;i++){
            int min=INF;
            int k;
            for(int j=1;j<=n;j++)//记录最小权值对应点
                if(mst[j]==0&&lowcost[j]<min){
                    min=lowcost[j];
                    k=j;
                }
            mst[k]=1;//加入该点
            //cout<<"-"<<k;
            sum+=lowcost[k];
            for(int j=1;j<=n;j++)//以k为起点更新权值
                if(mst[j]==0&&lowcost[j]>G[k][j])
                    lowcost[j]=G[k][j];
        }
        //cout<<endl;
        return sum;
    }
};
int main(){
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int n;
    while(cin>>n){
        Graph G(n);
        cout<<G.prim();
    }
    return 0;
}