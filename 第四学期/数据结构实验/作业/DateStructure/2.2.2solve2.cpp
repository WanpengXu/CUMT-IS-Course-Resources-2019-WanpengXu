#include <iostream>
#include "LinkedList.h"
using namespace std;
int main()
{
    LinkedList<int> A;
    cout<<"请输入结束标志：";
    int flag; cin>>flag;
    A.input(flag);cout<<endl;
    A.output(); cout<<endl;
    LinkedList<int> B;
    B.input(flag);cout<<endl;
    B.output(); cout<<endl;
    A=A+B;
    A.Sort();
    cout<<endl; A.output();
    return 0;
}