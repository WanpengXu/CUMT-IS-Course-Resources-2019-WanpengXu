#include <iostream>
using namespace std;
const int defaultSize=100;
template <typename T>	
class SeqList{
protected:
    T *data;       //顺序表存储数组
	int maxSize;	 //最大允许长度	
	int last; 	         //当前最后元素下标
	void reSize(int newSize);
public:
	SeqList ( int sz= defaultSize );
	SeqList(SeqList<T>& L);
	~SeqList ( ) { delete [ ] data; }	
	int Size()const{return maxSize;}	
	int Length ( ) const { return last+1; }
	int Search ( T& x ) const;//查找
	int Locate ( int i ) const;//定位
	bool getData(int i,T& x)const
	    {if(i>0&&i<=last+1) {x=data[i-1];return true; }else return false;}
	void setData (int i, T&  x)
	    {if(i>0 && i<=last+1) data[i-1]=x;  } 
	bool Insert (int i, T & x);//插入
	bool Remove (int i, T & x );//删除	
	int IsEmpty ( ) { return (last ==-1)?true:false; }	
	int IsFull ( ) { return (last == maxSize-1)?true:false; }
	void input();
	void output();
	SeqList<T> operator=(SeqList<T>& L);
};
template <typename T>
SeqList<T>::SeqList(int sz)
{
    if(sz>0)
    {
        maxSize=sz;
        last=-1;
        data=new T[maxSize];
        if(data==NULL)
            {cerr<<"存储分配错误！"<<endl;exit(1);}
    }
}
template <typename T>
void SeqList<T>::input()
{
    cout<<"开始建立顺序表，请输入表中元素个数：";
    int num;
    while(cin>>num)//num=last+1
    {
        if(last-1<=maxSize-1) break;
        cout<<"表元素个数输入有误，范围不能超过"<<maxSize-1<<"：";
    }
    last=num-1;
    for(int i=0;i<=last;i++)
    {
        cin>>data[i];
    }
}
template <typename T>
void SeqList<T>::output()
{
    cout<<"顺序表当前元素最后下标为："<<last<<endl;
    for(int i=0;i<=last;i++)
        cout<<"#"<<i+1<<":"<<data[i]<<'\t';
    cout<<endl;
}
template <typename T>
int SeqList<T>::Locate(int i)const
{
    if(i>=1&&i<=last+1) return i-1;
    else return 0;
}
template <typename T>
int SeqList<T>::Search(T&x)const
{
    for(int i=0;i<=last;i++)
        if(x==data[i]) return i+1;
    return 0;
}
template <typename T>
bool SeqList<T>::Insert(int i,T&x)
{
    if(last==maxSize-1) return false;
    if(i<0||i>last+1) return false;
    for(int j=last+1;j>=i+1;j--) data[j]=data[j-1];
    data[i]=x;
    last++;
    return true;
}
template <typename T>
bool SeqList<T>::Remove(int i,T&x)
{
    if(last==-1) return false;
    if(i<0||i>last+1) return false;
    x=data[i-1];
    for(int j=i;j<=last;j++)
        data[j-1]=data[j];
    last--;
    return true;
}
int main()
{
    int msz;
    cout<<"==构造函数测试，请输入顺序表容量，默认值为100==：";
    cin>>msz;
    SeqList<int> A(msz);
    cout<<endl<<"==input测试=="<<endl;
    A.input();//输入的其实是最后位置
    cout<<endl<<"==output测试=="<<endl;
    A.output();
    int a,temp;
    cout<<endl<<"==Locate测试，请输入待定位表项序号，将输出下标==：";
    cin>>a;
    cout<<A.Locate(a)<<endl;
    cout<<endl<<"==getData测试，将输出Locate测试中表项的值=="<<endl;
    A.getData(a,temp);
    cout<<temp<<endl;
    cout<<endl<<"==Search测试，将输出Locace测试中表项值的下标=="<<endl;
    cout<<A.Search(temp)<<endl;
    cout<<endl<<"==Size测试，将输出顺序表容量=="<<endl;
    cout<<A.Size()<<endl;
    cout<<endl<<"==Length测试，将输出顺序表长度=="<<endl;
    cout<<A.Length()<<endl;
    cout<<endl<<"==IsFull测试，将输出顺序表是否充满=="<<endl;
    cout<<boolalpha<<bool(A.IsFull())<<endl;
    cout<<endl<<"==IsEmpty测试，将输出顺序表是否为空=="<<endl;
    cout<<boolalpha<<bool(A.IsEmpty())<<endl;
    int b;
    cout<<endl<<"==setdata测试，请输入改变表项序号，将以Locate测试中的值替换==：";
    cin>>b;
    A.setData(b,temp);
    A.output();
    int c;
    cout<<endl<<"==Insert测试，请输入待后插表项序号，将以Locate测试中的值替换==：";
    cin>>c;
    A.Insert(c,temp);
    A.output();
    int d;
    cout<<endl<<"==Remove测试，请输入待移除表项==：";
    cin>>d;
    A.Remove(d,temp);
    A.output();
}