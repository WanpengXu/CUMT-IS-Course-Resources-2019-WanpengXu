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
    void insert(int e1, BSTNode* ptr) {
        if (e1 == ptr->data)
            return ;
        if (e1 < ptr->data) {
            if (!ptr->left)
                ptr->left = new BSTNode(e1);
            else
                insert(e1, ptr->left);
        }
        else {
            if (!ptr->right)
                ptr->right = new BSTNode(e1);
            else
                insert(e1, ptr->right);
        }
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
    while(cin>>n){
        n--;
        int val;
        cin>>val;
        BSTNode root(val);
        while(n--){
            cin>>val;
            bst.insert(val,&root);
        }
        bst.preOrder(&root);
        cout<<endl;
        bst.inOrder(&root);
        cout<<endl;
        bst.postOrder(&root);
        cout<<endl;
    }
    return 0;
}