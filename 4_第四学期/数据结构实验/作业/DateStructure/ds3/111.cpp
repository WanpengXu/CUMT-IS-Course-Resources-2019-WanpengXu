#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
const int INF = INT32_MAX;
const int MAXN = 1050;
struct Node {
	int v, w;
	Node(int a, int b) :v(a), w(b) {};
};
vector<Node> G[MAXN];
int d[MAXN], n, m, s, t, pre[MAXN];
bool vis[MAXN];

void Dijkstra() {
	fill(d, d + MAXN, INF);
	fill(vis, vis + MAXN, false);
	d[s] = 0;
	for (int i = 1; i <= n; i++) {
		int u = -1, MIN = INF;
		for (int j = 1; j <= n; j++) {
			if (!vis[j] && d[j] < MIN) {
				u = j;
				MIN = d[j];
			}
		}
		if (u == -1) return;
		vis[u] = true;
		for (int j = 0; j < G[u].size(); j++) {
			int v = G[u][j].v;
			if (!vis[v]) {
				if (d[u] + G[u][j].w < d[v]) {
					d[v] = d[u] + G[u][j].w;
					pre[v] = u;
				}
				else if (d[u] + G[u][j].w == d[v] && u < pre[v]) {
					pre[v] = u;
				}
			}
		}
	}
}
void DFS(int now) {
	if (now == s) {
		cout << s << " ";
		return;
	}
	DFS(pre[now]);
	cout << now << " ";//注意格式 最后有空格
}

int main() {
	while (cin >> n >> m >> s >> t) {//注意输入包含多组数据
		for (int i = 1; i <= n; ++i) G[i].clear();
		while (m--) {
			int u, v, w;
			cin >> u >> v >> w;
			G[u].push_back(Node(v, w));
			G[v].push_back(Node(u, w));
		}
		Dijkstra();
		if (d[t] == INF) cout << "can't arrive" << endl;
		else {
			cout << d[t] << endl;
			DFS(t);
		}
	}
	return 0;
}