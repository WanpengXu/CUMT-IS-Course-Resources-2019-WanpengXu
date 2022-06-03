#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>

using namespace std;

struct Node{
    int w;
    int v;
    Node(int a,int b){
        v=a;
        w=b;
    }
};

const int INF=INT32_MAX;
const int maxn=1000+10;
int des[maxn],pre[maxn];
vector<Node> G[maxn];
bool visited[maxn]={};
int N;

void Dijkstra(int s){
    fill(des,des+N+1,INF);
    for(int i=0;i<N;i++)
        pre[i]=i;
    visited[maxn]={};
    des[s]=0;
    for(int i=1;i<=N;i++){
        int min=INF,u=-1;
        for(int j=1;j<=N;j++){
            if(!visited[j]&&min>des[j]){
                min=des[j];
                u=j;
            }
        }
        if(u==-1)
            return ;
        visited[u]=true;
        for(int j=0;j<G[u].size();j++){
            int v=G[u][j].v;
            if(!visited[v]){
                if(des[v]>des[u]+G[u][j].w){
                    des[v]=des[u]+G[u][j].w;
                    pre[v]=u;
                }
                else if(des[v]==des[u]+G[u][j].w&&pre[v]>u)
                    pre[v]=u;
            }
        }
    }
}

void DFS(int s,int e){
    if(s==e){
        cout<<e<<" ";
        return ;
    }
    DFS(s,pre[e]);
    cout<<e<<" ";
}

int main(){
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int M,s,t;
    while(cin>>N>>M>>s>>t){
        for(int i=1;i<=N;i++)
            G[i].clear();
        for(int i=0,d=1;i<M;i++,d*=2){
            int u,v,w;
            cin>>u>>v>>w;
            G[u].push_back(Node(v,w));
            G[u].push_back(Node(u,w));
        }
        Dijkstra(s);
        if(des[t]!=INF){
            cout<<des[t]<<endl;
            DFS(s,t);
        }
        else
            cout<<"can't arrive";
        cout<<endl;
    }
    return 0;
}