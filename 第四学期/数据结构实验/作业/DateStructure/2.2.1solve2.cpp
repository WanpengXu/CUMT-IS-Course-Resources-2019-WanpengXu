#include "SeqList.h"
int main()
{
    SeqList<int> A;
    A.input(); cout<<endl;
    A.output(); cout<<endl;
    SeqList<int> B;
    B.input(); cout<<endl;
    B.output(); cout<<endl;
    A=A.extend(B);
    A.Sort();
    cout<<endl; A.output();
    return 0;
}