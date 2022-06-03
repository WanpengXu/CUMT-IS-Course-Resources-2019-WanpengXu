#include <iostream>
using namespace std;
struct JsNode{
    int data;//结点数据
    JsNode *link;//链接指针
    JsNode(JsNode *next=NULL):link(next){}
    JsNode(int item,JsNode *next=NULL):data(item),link(next){}
};
class JosephusCircle{
private: 
    JsNode *first, *last;
    int n,m;
public: 
    JosephusCircle(int n,int m);
    void Jskill();
    JsNode* Locate(int i);
    JsNode* getFirst();
};
JosephusCircle::JosephusCircle(int a,int b):n(a),m(b)
{
    last=first=new JsNode(0);
    //first->data=0;
    //last=first;
    for(int i=1;i<=n;i++)
    {
        if(first->data==0)//已有结点直接赋值
            first->data=i;
        else//新建结点并赋值
        {
            JsNode *newNode=new JsNode(i,first);
            //newNode->data=i;
            //newNode->link=first;
            last->link=newNode;
            last=newNode;
        }
    }
}
void JosephusCircle::Jskill() //问题在与n和m被清零了,已解决
{
    if(m<=0||m>n) cout<<"条件不合法！"<<endl;
    else
    {
        JsNode *p=getFirst(), *pre=NULL;//JsNode *p=Locate(1), *pre=NULL;
        for(int i=0;i<n-1;i++)
        {
            for (int j=1;j<m;j++) 
	            {
                    pre=p;
                    p=p->link; 
                }
            cout<<"出列的人是"<<p->data<<endl;
            pre->link=p->link;
            delete p;
            p=pre->link;                        
        }
    }
}
JsNode* JosephusCircle::Locate(int i)
{
    //if(i<0) return NULL;
    JsNode *current=first;
    int count=0;
    while(current->link!=first && count<i-1)
    {
        current=current->link;
        count++;
    }
    return current;
}
JsNode* JosephusCircle::getFirst(){
    return first;
}
int main()
{
    int n,m;		
    cout<<"输入游戏者人数和报数间隔:";
    cin>>n>>m;
    JosephusCircle clist(n,m);
    clist.Jskill();
    return 0;
}