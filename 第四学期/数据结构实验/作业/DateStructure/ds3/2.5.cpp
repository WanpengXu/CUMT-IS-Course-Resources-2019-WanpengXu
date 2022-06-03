#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <cfloat>
#include <map>

#define INF INT32_MAX
using namespace std;

struct node
{
    int w;
    int v;
    node(int a, int b) :v(a), w(b) {  };
};

const int MaxN = 1010;
int des[MaxN], pre[MaxN];
vector<node> G[MaxN];
bool visited[MaxN];
int N;

void Dijkstra(int s)
{
    fill(des, des + N + 1, INF);
    for (int i = 0; i < N; ++i)pre[i] = i;
    memset(visited, 0,N + 1);
    des[s] = 0;

    for (int i = 1,Min,u; i <= N; ++i)
    {
        Min = INF, u = -1;
        for (int k = 1; k <= N; ++k)
        {
            if (!visited[k] && Min > des[k])
            {
                Min = des[k];
                u = k;
            }
        }

        if (u == -1)return;
        visited[u] = true;

        for (int k = 0; k < G[u].size(); ++k)
        {
            int v = G[u][k].v;
            if(!visited[v])
            {
                if (des[v] > des[u] + G[u][k].w)
                {
                    des[v] = des[u] + G[u][k].w;
                    pre[v] = u;
                }
                else if (des[v] == des[u] + G[u][k].w && pre[v] > u)
                {
                    pre[v] = u;
                }
            }
        }
    }
}


void DFS(int s, int e)
{
    if (s == e)
    {
        cout << e << " ";
        return;
    }

    DFS(s, pre[e]);
    cout << e << " ";
}


int main()
{
#ifdef _DEBUG
    freopen("data.txt", "r+", stdin);
#endif // _DEBUG

    std::ios::sync_with_stdio(false);

    int M,s,t;
    while(cin >> N >> M >> s >> t)
    {
        for (int i = 1; i <= N; ++i)
            G[i].clear();

        for (int i = 0, d = 1; i < M; ++i, d *= 2)
        {
            int u, v, w;
            cin >> u >> v >> w;
            G[u].push_back(node(v, w));
            G[v].push_back(node(u, w));
        }

        Dijkstra(s);

        if (des[t] != INF)
        {
            cout << des[t] << endl;
            DFS(s, t);
        }
        else
            cout << "can't arrive";
       cout << endl;

    }

    return 0;
}
/**************************************************************
    Problem: 1987
    User: Sharwen
    Language: C++
    Result: 升仙
    Time:103 ms
    Memory:2396 kb
****************************************************************/