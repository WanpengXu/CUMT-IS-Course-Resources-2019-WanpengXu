#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn=1010;
const int INF=0x3fffffff;
bool vis[maxn];
int n,d[maxn],G[maxn][maxn];
vector<int> pre[maxn],temppath,path;
struct node
{
	int v,w;
	node(int x,int y):v(x),w(y){ };
};
vector<node> adj[maxn];
void Dijkstra(int s)
{
	fill(d,d+maxn,INF);
	fill(vis,vis+maxn,false);
	d[s]=0;
	for(int i=1;i<=n;++i)
	{
		int min=INF,u=-1;
		for(int j=1;j<=n;++j)
		{
			if(d[j]<min&&vis[j]==false)
			{
				u=j;
				min=d[j];
			}
		}
		if(u==-1)
			return ;
		vis[u]=true;
		for(int j=0;j<adj[u].size();++j)
		{
			int v=adj[u][j].v;
			if(vis[v]==false)
			{
				if(d[u]+adj[u][j].w<d[v])
				{
					d[v]=d[u]+adj[u][j].w;
					pre[v].clear();
					pre[v].push_back(u);
				}
				else if(d[u]+adj[u][j].w==d[v])
				{
					pre[v].push_back(u);
				}
			}
		}
	}
}
bool compare(vector<int> a,vector<int> b)
{
	int i=a.size()-1,j=b.size()-1;
	while(i>=0&&j>=0)
	{
		if(a[i]!=b[j])
			return a[i]<b[j];
		--i;--j;
	}
	return a.size()<b.size();
}
 
void DFS(int v,int s)
{
	if(v==s)
	{
		temppath.push_back(v);
		if(path.size()==0)
			path=temppath;
		else if(compare(temppath,path))
			path=temppath;
		temppath.pop_back();
		return ;
	}
	temppath.push_back(v);
	for(int i=0;i<pre[v].size();++i)
		DFS(pre[v][i],s);
	temppath.pop_back();
}
int main()
{
	int m,s,t,d1,d2,w;
    while(~scanf("%d %d %d %d",&n,&m,&s,&t))
    {
		for (int i=1;i<=n;++i)
            adj[i].clear();
        for(int i=0;i<m;++i)
        {
        	cin>>d1>>d2>>w;
        	adj[d1].push_back(node(d2,w));
        	adj[d2].push_back(node(d1,w));
		}
		Dijkstra(s);
		if(d[t]==INF)
		{
			cout<<"can't arrive"<<endl;
		}
		else
		{
			cout<<d[t]<<endl;
			temppath.clear();
			path.clear();
			DFS(t,s);
			for(int i=path.size()-1;i>=0;--i)
                cout<<path[i]<<(i>0?' ':'\n');
		}
    }
    return 0;
}