#include <iostream>
using namespace std;
struct BinTreeNode{
	int data;
	BinTreeNode *leftChild,*rightChild;
	BinTreeNode()
		:leftChild(NULL),rightChild(NULL){}
	BinTreeNode(int value,BinTreeNode *left=NULL,BinTreeNode *right=NULL)
		:data(value),leftChild(left),rightChild(right){}
};
class BinTree{
public:
	BinTreeNode *root;
	int refValue;
	BinTree(int value)
		:root(NULL),refValue(value){}
	void creatBinTree(BinTreeNode* &subTree);
	void posTraverse(BinTreeNode *subTree,void(*visit)(BinTreeNode *current));
	void inTraverse(BinTreeNode *subTree,void(*visit)(BinTreeNode *current));
	void postTraverse(BinTreeNode *subTree,void(*visit)(BinTreeNode *current));
	int height(BinTreeNode *subTree);
	int size(BinTreeNode *subTree);
	BinTreeNode* parent(BinTreeNode*subTree,BinTreeNode *current);
	bool isEmpty(BinTreeNode *subTree);
	friend void print(BinTreeNode *subTree);
};
void print(BinTreeNode *subTree){
	cout<<subTree->data<<' ';
}
void BinTree::creatBinTree(BinTreeNode* &subTree){
		int item;
		if(!cin.eof()){
			cin>>item;
			if(item!=refValue){
				subTree=new BinTreeNode(item);
				creatBinTree(subTree->leftChild);
				creatBinTree(subTree->rightChild);
			}
			else
				subTree=NULL;
		}
		else
			return ;
};
void BinTree::posTraverse(BinTreeNode *subTree,void(*visit)(BinTreeNode *current)){
		if(subTree!=NULL){
			visit(subTree);
			posTraverse(subTree->leftChild,visit);
			posTraverse(subTree->rightChild,visit);
		}
		else
			return ;
};
void BinTree::inTraverse(BinTreeNode *subTree,void(*visit)(BinTreeNode *current)){
		if(subTree!=NULL){
			inTraverse(subTree->leftChild,visit);
			visit(subTree);
			inTraverse(subTree->rightChild,visit);
		}
		else
			return ;
};
void BinTree::postTraverse(BinTreeNode *subTree,void(*visit)(BinTreeNode *current)){
		if(subTree!=NULL){
			postTraverse(subTree->leftChild,visit);
			postTraverse(subTree->rightChild,visit);
			visit(subTree);
		}
		else
			return ;
	}
int BinTree::height(BinTreeNode *subTree){
		if(subTree==NULL)
			return 0;
		else{
			int i=height(subTree->leftChild);
			int j=height(subTree->rightChild);
			return (i<j)?j+1:i+1;
		}
};
int BinTree::size(BinTreeNode *subTree){
		if(subTree==NULL)
			return 0;
		else
			return 1+size(subTree->leftChild)+size(subTree->rightChild);
};
BinTreeNode* BinTree::parent(BinTreeNode*subTree,BinTreeNode *current){
		if(subTree==NULL||subTree==current)
			return NULL;
		if(subTree->leftChild==current||subTree->rightChild==current)
			return subTree;
		BinTreeNode *p;
		if((p=parent(subTree->leftChild,current))!=NULL)
			return p;
		else
			return parent(subTree->rightChild,current);
};
bool BinTree::isEmpty(BinTreeNode *subTree){
		return root==NULL;
};
int main(){
	BinTree bt(0);
	bt.creatBinTree(bt.root);
	bt.posTraverse(bt.root,print);cout<<endl;
	bt.inTraverse(bt.root,print);cout<<endl;
	bt.postTraverse(bt.root,print);cout<<endl;
	cout<<bt.height(bt.root);cout<<endl;
	cout<<bt.size(bt.root);cout<<endl;
	cout<<bt.isEmpty(bt.root);cout<<endl;
	return 0;
}

//        1
//   2        3
//4     5        6
//         7
