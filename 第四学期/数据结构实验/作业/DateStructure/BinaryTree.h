template <class T>
class BinaryTree {
	//对象: 结点的有限集合, 二叉树是有序树
public:
	BinaryTree();			//构造函数
	BinaryTree(BinTreeNode<T>* lch,
		BinTreeNode<T>* rch, T item);
	//构造函数, 以item为根, lch和rch为左、右子
	//树构造一棵二叉树
	int Height();			//求树深度或高度
	int Size();			//求树中结点个数
	bool IsEmpty();		//判二叉树空否？ 
	BinTreeNode<T>* Parent(BinTreeNode<T>* t);
	//求结点 t 的双亲
	BinTreeNode<T>* LeftChild(BinTreeNode<T>* t);
	//求结点 t 的左子女
	BinTreeNode<T>* RightChild(BinTreeNode<T>* t);
	//求结点 t 的右子女
	bool Find(T& item);		//判断item是否在树中
	bool getData(T& item);	//取得结点数据
	bool Insert(T item);		//在树中插入新元素
	bool Remove(T item);	//在树中删除元素
	BinTreeNode<T>* getRoot();	//取根
	void preOrder(void (*visit) (BinTreeNode<T>* t));	//前序遍历, visit是访问函数
	void inOrder(void (*visit) (BinTreeNode<T>* t));
	//中序遍历, visit是访问函数
	void postOrder(void (*visit) (BinTreeNode<T>* t));
	//后序遍历, (*visit)是访问函数
	void levelOrder(void (*visit)(BinTreeNode<T>* t));
	//层次序遍历, visit是访问函数
};
