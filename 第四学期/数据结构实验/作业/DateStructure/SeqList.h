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
	SeqList (int sz= defaultSize);
	SeqList(SeqList<T>& L);
	~SeqList ( ) { delete [ ] data; }	
	int Size()const{return maxSize;}	
	int Length ( ) const { return last+1; }
	int Search (T& x) const;         //查找
	int Locate (int i) const;	        //定位
	bool getData(int i,T& x)const
	    {if(i>0&&i<=last+1) {x=data[i-1];return true; }else return false;}
	void setData (int i, T&  x)
	    {if(i>0 && i<=last+1) data[i-1]=x;  } 
	bool Insert (int i, T & x);       //插入
	bool Remove (int i, T & x );	       //删除	
	int IsEmpty ( ) { return (last ==-1)?true:false; }	
	int IsFull ( ) { return (last == maxSize-1)?true:false; }
	void input();
	void output();
    void Sort();
    SeqList<T> ordermerge(SeqList<T> &B);
    SeqList<T> extend(SeqList<T>& B);
	//SeqList<T> operator=(SeqList<T>& L);
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
    cout<<"当前顺序表元素最后下标为："<<last<<endl;
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
template <typename T>
void SeqList<T>::Sort()
{
    int len=Length();
    int i=0;
    int j=0;
    for(j=0;j<len;j++)
        for(i=0;i<j;i++)
            if(data[i]>data[i+1])
            {
                T temp=data[i];
                data[i]=data[i+1];
                data[i+1]=temp;
            }
}
template<typename T>
SeqList<T> SeqList<T>::extend(SeqList<T>& B)//其实是operate+
{
    int lenA=Length();
    int lenB=B.Length();
    int lenC=lenA+lenB;
    SeqList<T> C(lenC);
    int i;
    for(i=0;i<lenA;i++)
        C.data[i]=data[i];
    for(i=lenA;i<lenC;i++)
        C.data[i]=B.data[i-lenA];
    C.last=lenC-1;
    return C;
}
/*template<typename T>
SeqList<T> SeqList<T>::ordermerge(SeqList<T> &B)
{
    int i=0; int lenA=Length();
    int j=0; int lenB=B.Length();
    int lenC=lenA+lenB;
    SeqList<T> C(lenC);
    C.last=0;
    while(i<lenA&&j<lenB)
    {
        if(this->data[i]>B.data[j])
        {
            C.data[C.last]=B.data[j];
            j++;
            C.last++;
        }
        else
        {
            C.data[C.last]=this->data[i];
            i++;
            C.last++;
        }
    }
    while(i<lenA)
    {
        C.data[C.last]=this->data[i];
        i++;
        C.last++;
    }
    while(j<lenB)
    {
        C.data[C.last]=B.data[j];
        j++;
        C.last++;
    }
    return C;
}
*/
//参考
/*template<typename T>
void meger(SeqList<T> A, SeqList<T> B){
    int i=0,j=0,k;
    while(i< A.Length()){
        if (A.data[i] > B.data[B.Length()-1]) //若A->data[i]大于B中所有元素
        { 
            B.data[B.Length()]=A.data[i];  //将A->data[i]插入到B末尾
            B.Length()++; i++;
        }
        else if(A.data[i] < B.data[j]){
            for(k=B.Length()-1; k>=j; k--)
                B.data[k+1] = B.data[k]; //将元素B->data[j]及之后的元素依次后移
            B.data[j]=A.data[i]; //在位置j处插入
            B.Length()++; //顺序表长度加1
            i++; j++;
        }
        else j++;

    }
}
*/