template <class T>
class Tree {
    //对象: 树是由n (≥0) 个结点组成的有限集合。在
    //类界面中的 position 是树中结点的地址。在顺序
    //存储方式下是下标型, 在链表存储方式下是指针
    //型。T 是树结点中存放数据的类型, 要求所有结
    //点的数据类型都是一致的。
public:
    Tree();
    ~Tree();
    BuildRoot(const T& value);
    //建立树的根结点
    position FirstChild(position p);
    //返回 p 第一个子女地址, 无子女返回 0
    position NextSibling(position p);
    //返回 p 下一兄弟地址, 若无下一兄弟返回 0
    position Parent(position p);
    //返回 p 双亲结点地址, 若 p 为根返回 0
    T getData(position p);
    //返回结点 p 中存放的值
    bool InsertChild(position p, T& value);
    //在结点 p 下插入值为 value 的新子女, 若插
    //入失败, 函数返回false, 否则返回true
    bool DeleteChild(position p, int i);
    //删除结点 p 的第 i 个子女及其全部子孙结
    //点, 若删除失败, 则返回false, 否则返回true
    void DeleteSubTree(position t);
    //删除以 t 为根结点的子树
    bool IsEmpty();
    //判树空否, 若空则返回true, 否则返回false
    void Traversal(void (*visit)(position p));
    //遍历以 p 为根的子树
};
