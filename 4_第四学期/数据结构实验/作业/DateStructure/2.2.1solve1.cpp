#include "SeqList.h"

int main()
{
    SeqList<int> a;
    SeqList<int> b;
    a.input();a.output();cout<<endl;
    b.input();b.output();cout<<endl;
    meger(a,b);//不知道哪有问题，左值不能是新的？？？？？
    a.output();
    return 0;    
}