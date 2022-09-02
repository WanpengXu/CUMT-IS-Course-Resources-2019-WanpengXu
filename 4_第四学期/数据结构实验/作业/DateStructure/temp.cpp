#include <iostream>
#include "LinkedList.h"
template <typename T>
void List <T> :: MakeEmpty ( ) {
//删去链表中除附加头结点外的所有其他结点
//即把表变为有附加头结点的空表
    LinkNode<T> *q;
    while ( first->link != NULL ) {
 	    q = first->link;
        first->link = q->link;	//将表头结点后第一个结点q从链中摘下
	    delete q;        //释放它 
    }   
}
template <typename T>
void List <T> :: inputRear(T endTag ) {
    LinkNode<T> *newNode，*last，T val;
    makeEmpty();
    cin>>val;
    last=first;
    while (val != endTag) {
	    newNode = new LinkNode<T>(val);
	    if(newNode==NULL)
		    {cerr<<"error"<<endl;exit(1);}
	    last->link=newNode;
	    last=newNode;
	    cin>>val;
    }  
}
int main()
{
    List A(5);
    A.inputRear(0);
    return 0;
}
