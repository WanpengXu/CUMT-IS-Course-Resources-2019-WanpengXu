#include <iostream>
using namespace std;
template <typename T>  //结点结构定义
struct LinkNode {	
    T data; //结点数据 
    LinkNode<T> *link; //结点链接指针
    LinkNode(LinkNode<T> *ptr=NULL ) {link=ptr; }  //构造函数	
    LinkNode(const T& item,LinkNode<T> *ptr=NULL) {data=item;link=ptr;} 
    //如果有LinkNode<int> nd(x)  //则表示data=x，link=NULL   
}; 
template <typename T>  //链表类
class LinkedList{
protected:
    LinkNode<T> *first; //链表的头指针
public:
    LinkedList () { first = new LinkNode<T>; }
    LinkedList (const T& x) {first = new LinkNode<T> (x); }
    LinkedList (LinkedList<T>& L);
    //~LinkedList () { MakeEmpty(); }
    void MakeEmpty ( );	//将链表置为空表
    int Length( )const;	//计算链表的长度
    LinkNode<T> *getHead()const { return first; }
    LinkNode<T> *Search( T x );	//搜索含数据x的元素
    LinkNode<T> *Locate( int i ) const;//搜索第 i 个元素的地址
    bool GetData ( int i, T& x ) const;//取出表中第 i 个元素的值
    bool Insert (int i ,T& x);//将x插在表中第 i 个元素后
    void SetData(int i,T& x);
    bool Remove (int i ,T& x);//删除第i个元素，x返回该元素的值
    bool IsEmpty()const{ return first->link==NULL?true:false; }
    bool IsFull() const {return false;}
    void Sort();
    void input(T);
    void output();
    LinkedList<T>& extend(LinkedList<T>& L);
    LinkedList<T>& operator+(LinkedList<T>& L);
    //LinkedList<T>& operator=(LinkedList<T>& L);
};
template <typename T>
void LinkedList<T>::MakeEmpty()//有问题
{
    LinkNode<T> *current;
    while(first->link!=NULL)
    {
        current=first->link;
        first->link=current->link;
        delete current;
    }
}
template <typename T>
void LinkedList<T>::input(T endTag)
{
    LinkNode<T> *newNode,*last;
    T val;
    //MakeEmpty();
    cin>>val;
    last=first;
    while(val!=endTag)
    {
        newNode=new LinkNode<T>(val);
        if(newNode==NULL)
        {
            cerr<<"存储分配错误！"<<endl;
            exit(1);
        }
        last->link=newNode;
        last=newNode;
        cin>>val;
    }
    last->link=NULL;
}
template <typename T>
void LinkedList<T>::output()
{
    cout<<"当前单链表最后元素下标为"<<Length()-1<<endl;
    LinkNode<T> *current=first->link;
    int i=0;
    while(current!=NULL)
    {
        i++;
        cout<<'#'<<i<<':'<<current->data<<'\t';
        current=current->link;
    }
}
template <typename T>
bool LinkedList<T>::GetData(int i,T &x) const
{
    if(i<=0) return false;
    LinkNode<T> *current=Locate(i);
    if(current==NULL) return false;
    else
    {
        x=current->data;
        return true;
    }
}
template <typename T>
void LinkedList<T>::SetData(int i,T &x)
{
    if(i<=0) return;
    LinkNode<T> *current=Locate(i);
    if(current==NULL) return;
    else current->data=x;
}
template <typename T>
LinkNode<T>* LinkedList<T>::Locate(int i) const
{
    if(i<0) return NULL;
    LinkNode<T> *current=first;
    int k=0;
    while(current!=NULL&&k<i)
    {
        current=current->link;
        k++;
    }
    return current;
}
template <typename T>
LinkNode<T>* LinkedList<T>::Search(T x)
{
    LinkNode<T> *current=first->link;
    while(current!=NULL)
        if(current->data==x) break;
        else current=current->link;
    return current;
}
template <typename T>
int LinkedList<T>::Length() const
{
    LinkNode<T> *current=first->link;
    int count=0;
    while(current!=NULL)
    {
        current=current->link;
        count++;
    }
    return count;
}
template <typename T>
bool LinkedList<T>::Insert(int i,T &x)
{
    LinkNode<T> *current=Locate(i);
    if(current==NULL) return false;
    LinkNode<T> *newNode=new LinkNode<T>(x);
    if(newNode==NULL)
    {
        cerr<<"存储分配错误！"<<endl;
        exit(1);
    } 
    newNode->link=current->link;
    current->link=newNode;
    return true;
}
template <typename T>
bool LinkedList<T>::Remove(int i,T &x)
{
    LinkNode<T> *current=Locate(i-1);
    if(current==NULL||current->link==NULL) return false;
    LinkNode<T> *del=current->link;
    current->link=current->link->link;//current->link=del->link;
    x=del->data;
    delete del;
    return true;
}
template <typename T>
void LinkedList<T>::Sort()
{
    if(IsEmpty()) return;
    
    LinkNode<T> *currenti=first->link;
    LinkNode<T> *currentj=first->link;
    for(;currentj->link!=NULL;currentj=currentj->link)
        for(currenti=first->link;currenti->link!=NULL;currenti=currenti->link)
            if(currenti->data>currenti->link->data)
            {
                int temp=currenti->data;
                currenti->data=currenti->link->data;
                currenti->link->data=temp;
            }
}
template<typename T>
LinkedList<T>& LinkedList<T>::extend(LinkedList<T>& L)
{
    int len=Length();
    LinkNode<T> *last=Locate(len);
    last->link=L.first->link;
    return *this;
}
template<typename T>
LinkedList<T>& LinkedList<T>::operator+(LinkedList<T>& L)
{
    int len=Length();
    LinkNode<T> *last=Locate(len);
    last->link=L.first->link;
    return *this;
}