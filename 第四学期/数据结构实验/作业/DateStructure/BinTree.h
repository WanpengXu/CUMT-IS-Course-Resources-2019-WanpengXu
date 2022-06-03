#include <iostream>
using namespace std;
template <class T>
struct BinTreeNode {	      //二叉树结点类定义
    T data;	 		      //数据域
    BinTreeNode<T>* leftChild, * rightChild;    //左子女、右子女链域
    BinTreeNode()                //构造函数
    {
        leftChild = NULL;  rightChild = NULL;
    }
    BinTreeNode(T& x, BinTreeNode<T>* l = NULL,
        BinTreeNode<T>* r = NULL)
    {
        data = x;  leftChild = l;  rightChild = r;
    }
};
template <class T>
class BinaryTree {		//二叉树类定义
protected:
    BinTreeNode<T>* root; 	//二叉树的根指针
    T refValue;	 		//数据输入停止标志
public:
    BinaryTree() : root(NULL) { }	  //构造函数
    BinaryTree(T value) : refValue(value), root(NULL) { }
    BinaryTree(BinaryTree<T>& s);     //复制构造函数
    //～BinaryTree() { destroy(root); }	  //析构函数
    bool isEmpty() { return root == NULL; }//判二叉树空否
    int height() { return height(root); }  //求树高度

    BinTreeNode<T>* parent(BinTreeNode <T>* t)
    {
        return (root == NULL || root == t) ? NULL : parent(root, t);
    }  //返回双亲结点
    BinTreeNode<T>* leftChild(BinTreeNode<T>* t)
    {
        return (t != NULL)?t->leftChild : NULL;
    }
    //返回左子女
    BinTreeNode<T>* rightChild(BinTreeNode<T>* t)
    {
        return (t != NULL)?t->rightChild : NULL;
    }
    //返回右子女
    BinTreeNode<T>* getRoot() const { return root; }
    //取根
    void preOrder(void (*visit) (BinTreeNode<T>* t))           //前序遍历
    {
        preOrder(root, visit);
    }
    void inOrder(void (*visit) (BinTreeNode<T>* t))             //中序遍历
    {
        inOrder(root, visit);
    }
    void postOrder(void (*visit) (BinTreeNode<T>* t))         //后序遍历
    {
        postOrder(root, visit);
    }
    int size() const
    {
        return size(root);
    }
    void levelOrder(void (*visit)(BinTreeNode<T>* t));     //层次遍历
    int insert(const T item);	       //插入新元素	
    BinTreeNode<T>* find(T item) const;	  //搜索
protected:

    void createBinTree(istream& in, BinTreeNode<T>*& subTree) {
        //私有函数: 以递归方式建立二叉树。
        T item;
        if (!in.eof()) {	    	//未读完, 读入并建树	
            in >> item;  		//读入根结点的值
            if (item != refValue) {
                subTree = new BinTreeNode<T>(item); //建立根结点
                if (subTree == NULL)
                {
                    cerr << "存储分配错!" << endl;  exit(1);
                }
                createBinTree(in, subTree->leftChild);
                createBinTree(in, subTree->rightChild);
            }
            else subTree = NULL;    //封闭指向空子树的指针
        }
    }     //从文件读入建树
    bool insert(BinTreeNode<T>*& subTree, T& x);     //插入
    void destroy(BinTreeNode<T>*& subTree);     //删除
    bool find(BinTreeNode<T>* subTree, T& x);   // 查找	
    BinTreeNode<T>* copy(BinTreeNode<T>* r);	//复制
    int height(BinTreeNode<T>* subTree) const {
        //私有函数：利用二叉树后序遍历算法计算二叉
        //树的高度或深度
        if (subTree == NULL) return 0;	//空树高度为0
        else {
            int i = height(subTree->leftChild);
            int j = height(subTree->rightChild);
            return (i < j) ? j + 1 : i + 1;
        }
    }//返回树高度
    int size(BinTreeNode<T>* subTree) const;						             //返回结点数
    BinTreeNode<T>* parent(BinTreeNode<T>* subTree, BinTreeNode<T>* t);							             //返回父结点
    BinTreeNode<T>* find(BinTreeNode<T>* subTree, T& x) const;       //搜寻x
    void traverse(BinTreeNode<T>* subTree, ostream& out);	             //前序遍历输出
    void preOrder(BinTreeNode<T>& subTree, void (*visit) (BinTreeNode<T>* t));    //前序遍历
    void inOrder(BinTreeNode<T>& subTree, void (*visit) (BinTreeNode<T>* t));    //中序遍历
    void postOrder(BinTreeNode<T>& subTree, void (*visit) (BinTreeNode<T>* t));    //后序遍历
    friend istream& operator >> (istream& in, BinaryTree<T>& Tree);    //重载操作：输入
    friend ostream& operator << (ostream& out, BinaryTree<T>& Tree);    //重载操作：输出
};


template <class T>
void BinaryTree<T>::inOrder(BinTreeNode<T>& subTree, void (*visit) (BinTreeNode<T>* t)) {
    if (subTree != NULL) {
        inOrder(subTree->leftChild, visit);
        //遍历左子树
        visit(subTree);		//访问根结点
        inOrder(subTree->rightChild, visit);
        //遍历右子树
    }
};

template <class T>
void BinaryTree<T>::preOrder(BinTreeNode<T>& subTree, void (*visit) (BinTreeNode<T>* t)) {
    if (subTree != NULL) {
        visit(subTree);		//访问根结点
        preOrder(subTree->leftChild, visit);
        //遍历左子树
        preOrder(subTree->rightChild, visit);
        //遍历右子树
    }
};

template <class T>
void BinaryTree<T>::postOrder(BinTreeNode<T>& subTree, void (*visit) (BinTreeNode<T>* t)) {

    if (subTree != NULL) {
        postOrder(subTree->leftChild, visit);
        //遍历左子树
        postOrder(subTree->rightChild, visit);		                                        //遍历右子树
        visit(subTree);	         //访问根结点
    }
};

template <class T>
int BinaryTree<T>::size(BinTreeNode<T>* subTree) const {
    /*static int num;
    if (subTree == NULL)
            ;
    else
    {
        num++;
        size(subTree->leftChild);
        size(subTree->rightChild);
    }
    return num;
    */
    //利用二叉树后序遍历算法计算二叉树的结点个数
    if (subTree == NULL) return 0;	       //空树
    else return 1 + size(subTree->leftChild) + size(subTree->rightChild);
};

template<class T>
istream& operator >> (istream& in, BinaryTree<T>& Tree) {
    //重载操作: 输入并建立一棵二叉树Tree。in是输入流对象。
    createBinTree(in, Tree.root); 	//建立二叉树
    return in;
};

template <class T>
BinTreeNode<T>* BinaryTree<T>::parent(BinTreeNode <T>* subTree, BinTreeNode <T>* t) {
    //从结点 subTree 开始, 搜索结点 t 的双亲, 若找
               //到则返回双亲结点地址, 否则返回NULL
    if (subTree == NULL) return NULL;
    if (subTree->leftChild == t || subTree->rightChild == t)
        return subTree;	                 //找到, 返回父结点地址
    BinTreeNode <T>* p;
    if ((p = parent(subTree->leftChild, t)) != NULL)
        return p;	                              //递归在左子树中搜索
    else return parent(subTree->rightChild, t);
    //递归在右子树中搜索
};
template<class T>
void BinaryTree<T>::destroy(BinTreeNode<T>*& subTree) {
    //私有函数: 删除根为subTree的子树
    if (subTree != NULL) {
        destroy(subTree->leftChild);     //删除左子树
        destroy(subTree->rightChild);   //删除右子树
        delete subTree; 			 //删除根结点
    }
};
