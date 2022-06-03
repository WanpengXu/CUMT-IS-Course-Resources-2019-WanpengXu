//道理大家都懂，可能我的结构更清晰一点哈。
#include <iostream>
using namespace std;
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Tree {
public:
    void insert(int v, TreeNode* root) {
        if (v == root->val)
            return;//题目里说:输出的二叉树遍历序列中重复元素不用输出
        if (v < root->val) {//小于根节点，往左
            if (!root->left)
                root->left = new TreeNode(v);//左子树为空，以v值构造一个节点挂上去
            else
                insert(v, root->left);//左子树不为空，继续插入
        }
        else {//大于根节点，往右
            if (!root->right)
                root->right = new TreeNode(v);//右子树为空，以v值构造一个节点挂上去
            else
                insert(v, root->right);//右子树不为空，继续插入
        }
    }
    void preorderTraversal(TreeNode* root) {//前序遍历
        if (!root) return;
        cout << root->val << " ";
        preorderTraversal(root->left);
        preorderTraversal(root->right);
    }
    void inorderTraversal(TreeNode* root) {//中序遍历
        if (!root) return;
        inorderTraversal(root->left);
        cout << root->val << " ";
        inorderTraversal(root->right);
    }
    void postorderTraversal(TreeNode* root) {//后序遍历
        if (!root) return;
        postorderTraversal(root->left);
        postorderTraversal(root->right);
        cout << root->val << " ";
    }
};
int main() {
    int n;
    Tree tr;
    while (cin >> n) {
        n--;
        int val;
        cin >> val;
        TreeNode root(val);
        while (n--) {
            cin >> val;
            tr.insert(val, &root);
        }
        tr.preorderTraversal(&root); 
        cout << endl;
        tr.inorderTraversal(&root); 
        cout << endl;
        tr.postorderTraversal(&root); 
        cout << endl;
    }
    return 0;
}