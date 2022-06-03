#include <iostream>
using namespace std;
template <typename T>  //结点结构定义
struct LinkNode {	
    T data; //结点数据 
    LinkNode<T> *link; //结点链接指针
    LinkNode(LinkNode<T> *ptr=NULL ) {link=ptr; }  //构造函数	
    LinkNode (const T& item, LinkNode<T> *ptr=NULL ) {data=item;link=ptr;} 
    //如果有LinkNode<int> nd(x)  //则表示data=x，link=NULL   
}; 
template <typename T>  //链表类
class List{    
protected:
    LinkNode<T> *first; //链表的头指针
public:
    List () { first = new LinkNode<T>; }
    List (const T& x) {
	    first = new LinkNode<T> (x); }
    List (List<T>& L);
    ~List () { MakeEmpty(); }
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
    List<T>& operator=(List<T>& L);
};
template <typename T>
void List<T>::MakeEmpty()
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
void List<T>::input(T endTag)
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
void List<T>::output()
{
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
bool List<T>::GetData(int i,T &x) const
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
void List<T>::SetData(int i,T &x)
{
    if(i<=0) return;
    LinkNode<T> *current=Locate(i);
    if(current==NULL) return;
    else current->data=x;
}
template <typename T>
LinkNode<T>* List<T>::Locate(int i) const
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
LinkNode<T>* List<T>::Search(T x)
{
    LinkNode<T> *current=first->link;
    while(current!=NULL)
        if(current->data==x) break;
        else current=current->link;
    return current;
}
template <typename T>
int List<T>::Length() const
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
bool List<T>::Insert(int i,T &x)
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
bool List<T>::Remove(int i,T &x)
{
    LinkNode<T> *current=Locate(i-1);
    if(current==NULL||current->link==NULL) return false;
    LinkNode<T> *del=current->link;
    current->link=current->link->link;//current->link=del->link;
    x=del->data;
    delete del;
    return true;
}
int main()
{
    List<int> A;
    int flag;
    cout<<endl<<"==input测试，请输入结束标志后创建单链表==：";
    cin>>flag;
    A.input(flag);
    cout<<endl<<"==output测试=="<<endl;
    A.output();cout<<endl;
    int a,temp;
    cout<<endl<<"==Locate测试，请输入待定位表项序号，将输出地址==：";
    cin>>a;
    cout<<A.Locate(a)<<endl;
    cout<<endl<<"==GetData测试，将输出Locate测试中表项的值=="<<endl;
    A.GetData(a,temp);
    cout<<temp<<endl;
    cout<<endl<<"==Search测试，将输出Locace测试中表项值的地址=="<<endl;
    cout<<A.Search(temp)<<endl;
    cout<<endl<<"==Length测试，将输出单链表长度=="<<endl;
    cout<<A.Length()<<endl;
    cout<<endl<<"==IsEmpty测试，将输出单链表是否为空=="<<endl;
    cout<<boolalpha<<bool(A.IsEmpty())<<endl;
    int b;
    cout<<endl<<"==SetData测试，请输入改变表项序号，将以Locate测试中的值替换==：";
    cin>>b;
    A.SetData(b,temp);
    A.output();cout<<endl;
    int c;
    cout<<endl<<"==Insert测试，请输入待后插表项序号，将以Locate测试中的值替换==：";
    cin>>c;
    A.Insert(c,temp);
    A.output();cout<<endl;
    int d;
    cout<<endl<<"==Remove测试，请输入待移除表项==：";
    cin>>d;
    A.Remove(d,temp);
    A.output();cout<<endl;
    return 0;

}