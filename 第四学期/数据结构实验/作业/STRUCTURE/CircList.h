#include <iostream>
using namespace std;
template <typename T>//结点定义
struct CircLinkNode{
    T data;//结点数据
    CircLinkNode<T> *link;//链接指针
    CircLinkNode(CircLinkNode<T> *next=NULL):link(next){}
    CircLinkNode(T d,CircLinkNode<T> *next=NULL):data(d),link(next){}
};
template <typename T> 
class CircList{
private: 
    CircLinkNode<T> *first, *last;//链表的表头指针、当前指针和表尾指针
public: 
    CircList()
    {
        first=new CircLinkNode<T>;
        first->data=NULL;
        last=first;
    }
    CircList(const T& x)
    {
        first=new CircLinkNode<T>(x);
        last=first->link;
    }
    CircList(CircList<T>& L);			
    //~CircList();
    int Length() const;
    bool IsEmpty(){return first->link==first?true:false;}
    CircLinkNode<T>* getHead()const;
    void setHead(CircLinkNode<T> *p); 
    CircLinkNode<T>* Search(T x);
    CircLinkNode<T>* Locate(int i);
    T getData(int i);			
    void setData(int i,T& x);
    bool Insert(int i,T& x); 
    void Insert2(T& x);
    void output();
    bool Remove(int i,T& x);
};
template <typename T>  
bool CircList<T>::Insert(int i,T &x)
{
    CircLinkNode<T> *current=first->link;
    int count=0;
    while(current!=first && count<i-1)
    {
        current=current->link;
        count++;
    }
    if(current==first) return false;
    else
    {
        CircLinkNode<T> *newNode=new CircLinkNode<T>(x);
        //newNode->data=x;
        newNode->link=current->link;
        current->link=newNode;
        return true;
    }
}     
template <typename T>
CircLinkNode<T>* CircList<T>::Locate(int i)
{
    if(i<0) return NULL;
    CircLinkNode<T> *current=first;
    int count=0;
    while(current->link!=first && count<i-1)
    {
        current=current->link;
        count++;
    }
    return current;
}
template<typename T>
void CircList<T>::Insert2(T& x)
{
    if(first->data==NULL)//已有结点直接赋值
    {
        first->data=x;
    }
    else//新建结点并赋值
    {
        CircLinkNode<T>* newNode=new CircLinkNode<T>(x,first);
        //newNode->data=x;
        //newNode->link=first;
        last->link=newNode;
        last=newNode;
    }
}
template<typename T>
void CircList<T>::output()
{
    CircLinkNode<T> *current=first;
    int i=0;
    while(current->link!=first)
    {
        i++;
        cout<<'#'<<i<<':'<<current->data<<'\t';
        current=current->link;
    }
}
template <typename T>
T CircList<T>::getData(int i)
{
    if(i<=0) return NULL;
    CircLinkNode<T> *current=Locate(i);
    if(current==NULL) return NULL;
    else
    {
        T x=current->data;
        return x;
    }
}