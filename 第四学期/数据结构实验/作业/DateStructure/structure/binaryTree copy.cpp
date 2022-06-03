#include <iostream>
using namespace std;
struct BinTreeNode{
    char data;
    BinTreeNode *leftChild,*rightChild;
    BinTreeNode()
        :leftChild(NULL),rightChild(NULL){}
    BinTreeNode(char x,BinTreeNode *left=NULL,BinTreeNode *right=NULL)
        :data(x),leftChild(left),rightChild(right){}
};
class BinTree{
public:
    BinTreeNode* root;
    char refValue;
    BinTree():root(NULL){}
    BinTree(char value):refValue(value),root(NULL){}
    BinTreeNode* parent(BinTreeNode *subTree,BinTreeNode *current){
        if(subTree==NULL)
            return NULL;
        if(subTree->leftChild==current||subTree->rightChild==current)
            return subTree;
        BinTreeNode *p;
        if((p=parent(subTree->leftChild,current))!=NULL)
            return p;
        else
            return parent(subTree->rightChild,current);
    }
    void traverse(BinTreeNode *subTree,ostream& out){
        if(subTree!=NULL){
            out<<subTree->data;
            traverse(subTree->leftChild,out);
            traverse(subTree->rightChild,out);
        }
        return ;
    }
    BinTreeNode* search(const char x,BinTreeNode* subTree){
        if(subTree==NULL)
            return NULL;
        else if(x<subTree->data)
            return search(x,subTree->leftChild);
        else if(x>subTree->data)
            return search(x,subTree->rightChild);
        else
            return subTree;
    }
    bool insert(const char& x,BinTreeNode* &subTree){
        if(subTree==NULL){
            subTree=new BinTreeNode(x);
            return true;
        }
        else if(x<subTree->data)
            insert(x,subTree->leftChild);
        else if(x>subTree->data)
            insert(x,subTree->rightChild);
        else
            return false;
    }
    void preOrder(BinTreeNode *subTree,void(*visit)(BinTreeNode *current)){
        if(subTree!=NULL){
            visit(subTree);
            preOrder(subTree->leftChild,visit);
            preOrder(subTree->rightChild,visit);
        }
        return ;
    }
    void inOrder(BinTreeNode *subTree,void(*visit)(BinTreeNode *current)){
        if(subTree!=NULL){
            inOrder(subTree->leftChild,visit);
            visit(subTree);
            inOrder(subTree->rightChild,visit);
        }
        return ;
    }
    void postOrder(BinTreeNode *subTree,void(*visit)(BinTreeNode *current)){
        if(subTree!=NULL){
            postOrder(subTree->leftChild,visit);
            postOrder(subTree->rightChild,visit);
            visit(subTree);
        }
        return ;
    }
    int size(BinTreeNode *subTree)const{
        if(subTree==NULL)
            return 0;
        else
            return 1+size(subTree->leftChild)+size(subTree->rightChild);
    }
    int height(BinTreeNode *subTree)const{
        if(subTree==NULL)
            return 0;
        else{
            int i=height(subTree->leftChild);
            int j=height(subTree->rightChild);
            return (i<j)?j+1:i+1;
        }
    }
    void creatBinTree(BinTreeNode* &subTree){
        int item;
        if(!cin.eof()){
            cin>>item;
            if(item!=refValue){
                subTree=new BinTreeNode(item);
                creatBinTree(subTree->leftChild);
                creatBinTree(subTree->rightChild);
            }
        }
        else
            subTree=NULL;
    }
    void destroy(BinTreeNode* &subTree){
        if(subTree!=NULL){
            destroy(subTree->leftChild);
            destroy(subTree->rightChild);
            delete subTree;
        }
        return ;
    }
    void print(BinTreeNode* subTree){
        cout<<subTree->data;
        return ;
    }
};
ostream& operator << (ostream& out,BinTree& tree){
    tree.traverse(tree.root,out);
    out<<endl;
    return out;
    }
istream& operator>>(istream& in,BinTree& tree){
    tree.creatBinTree(tree.root);
    return in;
}
int main(){
    BinTree bt('#');
    cin>>bt;
    cout<<bt;
    return 0;
}