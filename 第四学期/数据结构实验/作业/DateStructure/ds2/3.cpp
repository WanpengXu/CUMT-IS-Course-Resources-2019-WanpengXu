#include <iostream>
using namespace std;

const int maxWeight = 2147483647;
const int DefaultVertices = 30;

template <class T, class E>
struct Edge {			   //边结点的定义
    int dest;				   //边的另一顶点位置
    E cost;				   //边上的权值
    Edge<T, E>* link;		   //下一条边链指针
    Edge() {}				   //构造函数
    Edge(int num, E weight) 	   //构造函数
        : dest(num), cost(weight), link(NULL) { }
    bool operator != (Edge<T, E>& R) const
    {
        return dest != R.dest;
    }	   //判边等否
};
template <class T, class E>
struct Vertex {			   //顶点的定义
    T data;				   //顶点的名字
    Edge<T, E>* adj;		   //边链表的头指针
};

template <class T, class E>
class Graphlnk{   //图的类定义
private:
    Vertex<T, E>* NodeTable;//顶点表 (各边链表的头结点)

    int maxVertices;
    int numVertices;
    int numEdges;

    
public:
    Graphlnk(int sz = DefaultVertices);  //构造函数
    ~Graphlnk();				   //析构函数
    int getVertexPos(const T vertx) {
        //给出顶点vertex在图中的位置
        for (int i = 0; i < numVertices; i++)
            if (NodeTable[i].data == vertx) return i;
        return -1;
    }
    T getValue(int i) {		     //取顶点 i 的值
        return (i >= 0 && i < numVertices) ? NodeTable[i].data : 0;
    }
    E getWeight(int v1, int v2);	     //取边(v1,v2)权值
    int NumberOfVertices() {
        return numVertices;
    }
    int NumberOfEdges() {
        return numEdges;
    }
    bool insertVertex(const T& vertex);
    bool insertEdge(int v1, int v2, E cost);
    int getFirstNeighbor(int v);
    int getNextNeighbor(int v, int w);
    friend istream& operator >> <>(istream& in, Graphlnk<T, E>& G);
    template <typename T, class E>
    friend ostream& operator << (ostream& out, Graphlnk<T, E>& G);
};
template <class T, class E>
Graphlnk<T, E>::Graphlnk(int sz) {
    //构造函数：建立一个空的邻接表
    maxVertices = sz;
    numVertices = 0;  numEdges = 0;
    NodeTable = new Vertex<T, E>[maxVertices];		//创建顶点表数组
    if (NodeTable == NULL)
    {
        cerr << "存储分配错！" << endl;  exit(1);
    }
    for (int i = 0; i < maxVertices; i++)
        NodeTable[i].adj = NULL;
};
template <class T, class E>
Graphlnk<T, E>::~Graphlnk() {
    //析构函数：删除一个邻接表
    for (int i = 0; i < numVertices; i++) {
        Edge<T, E>* p = NodeTable[i].adj;
        while (p != NULL) {
            NodeTable[i].adj = p->link;
            delete p;  p = NodeTable[i].adj;
        }
    }
    delete[]NodeTable;  		     //删除顶点表数组
};

template <typename T,class E>
E Graphlnk<T, E>::getWeight(int v1, int v2) {
    if (v1 != -1 && v2 != -1) {
        Edge<T, E>* p = NodeTable[v1].adj;
        while (p != NULL && p->dest != v2) {
            p = p->link;
        }
        if (p != NULL) {
            return p->cost;
        }
    }
}

template <typename T,class E>
bool Graphlnk<T, E>::insertVertex(const T& vertex) {
    if (numVertices == maxVertices) {
        return false;
    }
    NodeTable[numVertices].data = vertex;
    numVertices++;
    return true;
}

template <typename T,class E>
bool Graphlnk<T, E>::insertEdge(int v1,int v2,E weight){
    if (v1 >= 0 && v1 < numVertices && v2 >= 0 && v2 < numVertices) {
        Edge<T, E>* q, * p = NodeTable[v1].adj;
        while (p != NULL && p->dest != v2) {
            p = p->link;
        }
        if (p != NULL) {
            return false;
        }
        p = new Edge<T, E>;
        q = new Edge<T, E>;
        p->dest = v2;
        p->cost = weight;
        p->link = NodeTable[v1].adj;
        NodeTable[v1].adj = p;
        q->dest = v1;
        q->cost = weight;
        q->link = NodeTable[v2].adj;
        NodeTable[v2].adj = q;
        numEdges++;
        return true;
    }
    return 0;
}
template <class T, class E>
int Graphlnk<T, E>::getFirstNeighbor(int v) {
    //给出顶点位置为 v 的第一个邻接顶点的位置, 
    //如果找不到, 则函数返回-1
    if (v != -1) {			//顶点v存在
        Edge<T, E>* p = NodeTable[v].adj;			//对应边链表第一个边结点
        if (p != NULL) return p->dest;				//存在, 返回第一个邻接顶点
    }
    return -1;		//第一个邻接顶点不存在
};
template <class T, class E>
int Graphlnk<T, E>::getNextNeighbor(int v, int w) {
    //给出顶点v的邻接顶点w的下一个邻接顶点的位置,
    //若没有下一个邻接顶点, 则函数返回-1
    if (v != -1) {				//顶点v存在
        Edge<T, E>* p = NodeTable[v].adj;
        while (p != NULL && p->dest != w)
            p = p->link;
        if (p != NULL && p->link != NULL)
            return p->link->dest; 	//返回下一个邻接顶点
    }
    return -1; 			//下一邻接顶点不存在
};

template<typename T, class E>
istream& operator >> (istream& in, Graphlnk<T, E>& G) {
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

template <typename T, class E>
ostream& operator << (ostream& out, Graphlnk<T, E>& G) {
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

template<typename T, class E>
void DFSTraverse(Graphlnk<T, E>& G, const T& v) {
    //从顶点v出发对图G进行深度优先遍历的主过程
    int i, loc, n = G.NumberOfVertices();    //顶点个数
    bool* visited = new bool[n];          //创建辅助数组
    for (i = 0; i < n; i++) visited[i] = false; //辅助数组初始化

    loc = G.getVertexPos(v);
    DFS(G, loc, visited); //从顶点0开始深度优先搜索
    delete[] visited;			        //释放visited
}

template<typename T, class E>
void DFS(Graphlnk<T, E>& G, int v, bool visited[]) {
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
    Graphlnk<char,int> Gra;
    cin >> Gra;
    char start;
    cin >> start;
    DFSTraverse(Gra, start);
    return 0;
}