#include <iostream>
using namespace std;
struct LinkNode {    
    int  data;		       
    LinkNode * link;          	
}; 
class List{
    private:
        LinkNode * first;
    public:
        void inputRear(int endTag=0)
        {
            LinkNode *newNode,*last;
            int val;
            cin>>val;
            last=first;
            while(val!=endTag)
            {
                newNode=new LinkNode;
                newNode->data=val;
                last->link=newNode;
                last=newNode;
                cin>>val;
            }
            last->link=NULL;
        }
        void leftdelete(int &x)
        {
            LinkNode *del,*p=first;
            while(p!=NULL)
                if(p->link->link->data==x) break;
                else p=p->link;
            del=p->link;
            p->link=del->link;
            delete del;
        }
        void show()
        {
            LinkNode *p;
            p=first;
            while(p)
            {
                cout<<p->data<<' ';
                p=p->link;
            }
            cout<<endl;
        }
};
int main()
{
    List A;
    A.inputRear();
    /*cout<<'o';
    int a;
    cin>>a;
    A.leftdelete(a);*/
    A.show();
    return 0;
}