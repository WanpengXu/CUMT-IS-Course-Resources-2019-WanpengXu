#include <iostream>
#include "CircList.h"
template <typename T> 
void Josephus (CircList<T>& Js, int n, int m ) {
    CircLinkNode<T> *p=Js.Locate(1), *pre=NULL;
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
int main()
{
    CircList<int> clist;
    int n,m;		
    cout<<"输入游戏者人数和报数间隔:";
    cin>>n>>m;
    for(int i=1;i<=n;i++)
        clist.Insert2(i);
    Josephus(clist,n,m);
    return  0;
}
