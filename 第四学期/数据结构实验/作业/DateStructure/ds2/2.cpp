#include <iostream>
using namespace std;

const int maxWeight = 2147483647;
const int DefaultVertices = 30;

template <class T, class E>
class Graphmtx{
    friend istream& operator >> (istream& in, Graphmtx<T, E>& G);
    friend ostream& operator << (ostream& out, Graphmtx<T, E>& G);
private:
	T* VerticesList; 			//顶点表
	E** Edge;				//邻接矩阵
    int maxVertices;
    int numVertices;
    int numEdges;
	
public:
    Graphmtx(int sz = DefaultVertices);    //构造函数
    T getValue(int i) {
        //取顶点 i 的值, i 不合理返回0
        return i >= 0 && i <= numVertices ?
            VerticesList[i] : NULL;
    }
    E getWeight(int v1, int v2) {  //取边(v1,v2)上权值
        return v1 != -1 && v2 != -1 ? Edge[v1][v2] : 0;
    }
    int getVertexPos(T vertex) {
        //给出顶点vertex在图中的位置
        for (int i = 0; i < numVertices; i++)
            if (VerticesList[i] == vertex)
                return i;
        return -1;
    }
    int NumberOfVertices() {
        return numVertices;
    }
    int NumberOfEdges() {
        return numEdges;
    }
    int getFirstNeighbor(int v);  //取顶点 v 的第一个邻接顶点
    int getNextNeighbor(int v, int w);  //取 v 的邻接顶点 w 的下一邻接顶点
    bool insertVertex(const T vertex);  //插入顶点vertex
    bool insertEdge(int v1, int v2, E cost);  //插入边(v1, v2),权值为cost
};

template<typename T,class E>
istream& operator >> (istream& in, Graphmtx<T, E>& G) {
    int i, j, k, n, m;
    T e1, e2;
    E weight;
    in >> n >> m;
    for (i = 0; i < n; i++) {
        in >> e1;
        G.insertVertex(e1);
    }
    i = 0;
    while (i < m) {
        in >> e1 >> e2 >> weight;
        j = G.getVertexPos(e1);
        k = G.getVertexPos(e2);
        if (j == -1 || k == -1) {
            cout << "边两端点信息有误，重新输入！" << endl;
        }
        else {
            G.insertEdge(j, k, weight);
            i++;
        }
    }
    return in;
}

template <typename T,class E>
ostream& operator << (ostream& out, Graphmtx<T, E>& G) {
    int i, j, k, n, m;
    T e1, e2;
    E weight;
    n = G.NumberOfVertices();
    m = G.NumberOfEdges();
    out << n << "," << m << endl;
    for (i = 0; i < n; i++) {
        for (j = i + 1; j < n; j++) {
            weight = G.getWeight(i, j);
            if (weight > 0 && weight < maxWeight) {
                e1 = G.getValue(i);
                e2 = G.getValue(j);
                out << "(" << e1 << "," << e2 << "," << weight << ")" << endl;
            }
        }
    }
    return out;
}

template <class T, class E>
Graphmtx<T, E>::Graphmtx(int sz) {      //构造函数
    maxVertices = sz;
    numVertices = 0;  numEdges = 0;
    int i, j;
    VerticesList = new T[maxVertices];  //创建顶点表
    Edge = (E**) new E * [maxVertices];
    for (i = 0; i < maxVertices; i++)
        Edge[i] = new E[maxVertices];   //邻接矩阵 
    for (i = 0; i < maxVertices; i++)        //矩阵初始化
        for (j = 0; j < maxVertices; j++)
            Edge[i][j] = (i == j)? 0 : maxWeight;
};

template <class T, class E>
int Graphmtx<T, E>::getFirstNeighbor(int v) {
    //给出顶点位置为v的第一个邻接顶点的位置, 
    //如果找不到, 则函数返回-1
    if (v != -1) {
        for (int col = 0; col < numVertices; col++)
            if (Edge[v][col] && Edge[v][col] < maxWeight)
                return col;
    }
    return -1;
};

template <class T, class E>
int Graphmtx<T, E>::getNextNeighbor(int v, int w) {
    //给出顶点 v 的某邻接顶点 w 的下一个邻接顶点 
    if (v != -1 && w != -1) {
        for (int col = w + 1; col < numVertices; col++)
            if (Edge[v][col] && Edge[v][col] < maxWeight)
                return col;
    }
    return -1;
};

template<typename T,class E>
bool Graphmtx<T, E>::insertVertex(const T vertex){
    if (numVertices == maxVertices)
        return false;
    VerticesList[numVertices++] = vertex;
    return true;
}

template <typename T,class E>
bool Graphmtx<T, E>::insertEdge(int v1, int v2, E cost) {
    if (v1 > -1 && v1<numVertices && v2>-1 && v2 < numVertices && Edge[v1][v2] == maxWeight) {
        Edge[v1][v2] = Edge[v2][v1] = cost;
        numEdges++;
        return true;
    }
    else
        return false;
}

template<typename T, class E>
void DFSTraverse(Graphmtx<T, E>& G, const T& v) {
    //从顶点v出发对图G进行深度优先遍历的主过程
    int i, loc, n = G.NumberOfVertices();    //顶点个数
    bool* visited = new bool[n];          //创建辅助数组
    for (i = 0; i < n; i++) visited[i] = false; //辅助数组初始化

    loc = G.getVertexPos(v);
    DFS(G, loc, visited); //从顶点0开始深度优先搜索
    delete[] visited;			        //释放visited
}

template<typename T, class E>
void DFS(Graphmtx<T, E>& G, int v, bool visited[]) {
    cout << G.getValue(v) << ' ';        //访问顶点v
    visited[v] = true;	 	         //作访问标记
    int w = G.getFirstNeighbor(v);     //第一个邻接顶点
    while (w != -1) {	//若邻接顶点w存在
        if (!visited[w]) DFS(G, w, visited);
        //若w未访问过, 递归访问顶点w
        w = G.getNextNeighbor(v, w); //下一个邻接顶点
    }
}

int main() {
    Graphmtx<char,int> Gra;
    cin >> Gra;
    cout << Gra;
    char start;
    cin >> start;
    DFSTraverse(Gra,start);
    return 0;
}