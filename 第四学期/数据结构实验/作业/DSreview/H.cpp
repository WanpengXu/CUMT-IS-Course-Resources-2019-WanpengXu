#include <iostream>
using namespace std;
int n,sum,e[55][55],dis[55],book[55];
const int INF=INT32_MAX;
void prim(){
    for(int i=1;i<=n;i++){
        dis[i]=e[1][i];
        book[i]=0;
    }
    dis[1]=0;
    book[1]=1;
    for(int i=1;i<n;i++){
        int min=INF;
        int k;
        for(int j=1;j<=n;j++){
            if(book[j]==0&&dis[j]<min){
                min=dis[j];
                k=j;
            }
        }
        book[k]=1;
        sum+=dis[k];
        for(int j=1;j<=n;j++)
            if(book[j]==0&&dis[j]>e[k][j])
                dis[j]=e[k][j];
    }
    return ;
}
int main(){
    while(cin>>n){
        sum=0;
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++){
                cin>>e[i][j];
                if(i!=j&&e[i][j]==0)
                    e[i][j]=INF;
            }
        prim();
        cout<<sum<<endl;
    }
    return 0;
}