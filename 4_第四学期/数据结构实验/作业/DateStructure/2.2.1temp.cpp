#include "SeqList.h"
template<typename T>
SeqList<T> ordermerge(SeqList<T>& A,SeqList<T>& B)
{
    int i = 0;
    int j = 0;
    int k = 0;
    SeqList<T> C;
    while (i < A.Length() && j < B.Length())
    {
        if (A.data[i] >= B.data[j])
        {
            C.data[k] = B.data[j];
            j++;
            k++;
        }
        else
        {
            C.data[k] = A.data[i];
            i++;
            k++;
            C.output();
        }
    }
    while (i < A.Length())
    {
        cout<<C.data[0]<<endl;
        C.data[k] = A.data[i];
        i++;
        k++;
        C.output();
    }
    while (j < B.Length())
    {
        cout<<C.data[0]<<endl;
        C.data[k] = B.data[j];
        j++;
        k++;
        C.output();
    }
    C.last = k;
    C.output();
    return C;
}
int main()
{
    SeqList<int> a;
    SeqList<int> b;
    a.input(); a.output(); cout << endl;
    b.input(); b.output(); cout << endl;
    //cout<<a.data[0]<<endl;
    a=ordermerge(a,b);
    //cout<<a.data[0]<<endl;
    a.output();
    return 0;
}