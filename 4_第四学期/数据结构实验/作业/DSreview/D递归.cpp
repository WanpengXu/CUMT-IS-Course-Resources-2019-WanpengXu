#include <iostream>
using namespace std;
struct BSTNode{
    int data;
    BSTNode *left,*right;
    BSTNode(int d,BSTNode *L=NULL,BSTNode *R=NULL)
        :data(d),left(L),right(R){}
};
class BST{
public:
    bool insert(int e1,BSTNode*& ptr){
        if(ptr==NULL){
            ptr=new BSTNode(e1);
            if(ptr==NULL){
                cerr<<"Out of space"<<endl;
                exit(1);
            }
            return true;
        }
        else if(e1<ptr->data)
            insert(e1,ptr->left);
        else if(e1>ptr->data)
            insert(e1,ptr->right);
        else
            return false;
    }
    void preOrder(BSTNode* subTree){
        if(subTree!=NULL){
            cout<<subTree->data<<" ";
            preOrder(subTree->left);
            preOrder(subTree->right);
        }
    }
    void inOrder(BSTNode* subTree){
        if(subTree!=NULL){
            inOrder(subTree->left);
            cout<<subTree->data<<" ";
            inOrder(subTree->right);
        }
    }
    void postOrder(BSTNode* subTree){
        if(subTree!=NULL){
            postOrder(subTree->left);
            postOrder(subTree->right);
            cout<<subTree->data<<" ";
        }
    }
};
int main(){
    ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int n;
    BST bst;
    BSTNode *root;
    while(cin>>n){
        root=NULL;
        int num;
        for(int i=0;i<n;i++){
            cin>>num;
            bst.insert(num,root);
        }
        bst.preOrder(root);
        cout<<endl;
        bst.inOrder(root);
        cout<<endl;
        bst.postOrder(root);
        cout<<endl;
        
    }
    return 0;
}