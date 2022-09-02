#include <iostream>                            //P88栈的类定义
using namespace std;
const int stackIncrement=20;

template <class T>
class SeqStack{     //顺序栈类定义
private:     
    T *elements;			       //栈元素存放数组
    int top;				                    //栈顶指针
    int maxSize;               		                //栈最大容量
    void overflowProcess();	            //栈的溢出处理
public:
    SeqStack(int sz=50)
        :top(-1),maxSize(sz){
            elements=new T[maxSize];
        }		              //构造函数
    ~SeqStack(){
        delete []elements;
    }   //析构函数
    void push(T x);	//进栈  书上参数为 ( const T& x)
    bool pop(T &x);		                      //出栈
    bool getTop(T &x);		           //取栈顶内容
    bool isEmpty()const{
        return top==-1;
    }
    bool isFull()const{
        return top==maxSize-1;
    }
    int getSize()const{
        return top+1 ;
    }
    void makeEmpty( ){
        top=-1;
    }
};
template <class T>
void SeqStack<T>::overflowProcess() {
         //私有函数：当栈满则执行扩充栈存储空间处理
    T *newArray=new T[maxSize+stackIncrement];	//创建更大的存储数组   if(newArray==NULL){cerr<<“失败”<<endl; exit(1); }
	for(int i=0;i<=top;i++) 
        newArray[i]=elements[i];
	maxSize+=stackIncrement;
    delete []elements;
    elements=newArray;  	  //改变elements指针
};
template <class T>
void SeqStack<T>::push(T x) {
//若栈不满, 则将元素x插入该栈栈顶, 否则溢出处理
	if(isFull()==true)
        overflowProcess();	      //栈满
	elements[++top]=x;	     //栈顶指针先加1, 再进栈
}; 
template <class T>
bool SeqStack<T>::pop(T& x) {
//函数退出栈顶元素并返回栈顶元素的值
	if(isEmpty()==true)
        return false;
	x=elements[top--];//先取值，然后栈顶指针减1
    return true;		                            //退栈成功
};

template <class T>
bool SeqStack<T>::getTop(T& x) {//若栈不空则函数返回该栈栈顶元素的地址
	if (isEmpty()==true)
        return false;
	x=elements[top];
    return true;
};
int main(){
    SeqStack<int> stk(10);
    int N;
    cin>>N;
    for(int i=0;i<N;i++){
        int n;
        cin>>n;
        stk.push(n);
    }
    for(int i=0;i<N;i++){
        int n;
        stk.pop(n);
        cout<<n<<' ';
    }
    return 0;
}