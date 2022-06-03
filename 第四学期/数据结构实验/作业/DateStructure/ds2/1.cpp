#include <iostream>
#include <cstring>
using namespace std;

template <typename T>
struct BinTreeNode {
    T data;
    BinTreeNode<T>* leftChild, * rightChild;
    BinTreeNode() {
        leftChild = NULL;
        rightChild = NULL;
    }
    BinTreeNode(T& x, BinTreeNode<T>* l = NULL, BinTreeNode<T>* r = NULL) {
        data = x;
        leftChild = l;
        rightChild = r;
    }
};
template <typename T>
class BinaryTree {
protected:
    BinTreeNode<T>* root;
    T RefValue;
public:
    BinaryTree() : root(NULL) { }
    BinaryTree(T value) : RefValue(value), root(NULL) { }
    BinTreeNode<T>* LeftChild(BinTreeNode<T>* t) {
        return (t != NULL) ? t->leftChild : NULL;
    }
    BinTreeNode<T>* RightChild(BinTreeNode<T>* t) {
        return (t != NULL) ? t->rightChild : NULL;
    }
    void preOrder() {
        preOrder(root);
    }
    void inOrder() {
        inOrder(root);
    }
    void postOrder() {
        inOrder(root);
    }
    int size() {
        return size(root);
    }
    int leafSize() {
        return leafSize(root);
    }
protected:
    void CreateBinTree(istream& in, BinTreeNode<T>*& subTree);
    void preOrder(BinTreeNode<T>* subTree);
    void inOrder(BinTreeNode<T>* subTree);
    void postOrder(BinTreeNode<T>* subTree);
    int size(BinTreeNode<T>* subTree);
    int leafSize(BinTreeNode<T>* subTree);
    friend istream& operator >> (istream& in, BinaryTree<T>& Tree) {
        Tree.CreateBinTree(in, Tree.root);
        return in;
    }
    friend ostream& operator << (ostream& out, BinaryTree<T>& Tree) {
        Tree.preOrder();
        return out;
    }
};

template<typename T>
void BinaryTree<T>::CreateBinTree(istream& in, BinTreeNode<T>*& subTree) {
    T item;
    if (!in.eof()) {
        in >> item;
        if (item != RefValue) {
            subTree = new BinTreeNode<T>(item);
            if (subTree == NULL){
                cerr << "存储分配错!" << endl; exit(1);
            }
            CreateBinTree(in, subTree->leftChild);
            CreateBinTree(in, subTree->rightChild);
        }
        else
            subTree = NULL;
    }
}

template<typename T>
void BinaryTree<T>::preOrder(BinTreeNode<T>* subTree) {
    if (subTree) {
        cout << subTree->data;
        preOrder(subTree->leftChild);
        preOrder(subTree->rightChild);
    }
}

template<typename T>
void BinaryTree<T>::inOrder(BinTreeNode<T>* subTree) {
    if (subTree) {
        preOrder(subTree->leftChild);
        cout << subTree->data;
        preOrder(subTree->rightChild);
    }
}

template<typename T>
void BinaryTree<T>::postOrder(BinTreeNode<T>* subTree) {
    if (subTree) {
        preOrder(subTree->leftChild);
        cout << subTree->data;
        preOrder(subTree->rightChild);
    }
}

template<typename T>
int BinaryTree<T>::size(BinTreeNode<T>* subTree) {
    if (subTree == NULL) {
        return 0;
    }
    else
        return 1 + size(subTree->leftChild) + size(subTree->rightChild);
}

template<typename T>
int BinaryTree<T>::leafSize(BinTreeNode<T>* subTree) {
    if (subTree == NULL) {
        return 0;
    }
    else if (subTree->leftChild == NULL && subTree->rightChild == NULL) {
        return 1;
    }
    else {
        return leafSize(subTree->leftChild) + leafSize(subTree->rightChild);
    }
}

#include <iostream>
using namespace std;
int main() {
	BinaryTree<char> A('0');
	cin >> A;
    cout << A << endl;
    A.inOrder();
    cout << endl;
    A.postOrder();
    cout << endl;
    cout << A.size() << endl;
    cout << A.leafSize() << endl;
	return 0;
}