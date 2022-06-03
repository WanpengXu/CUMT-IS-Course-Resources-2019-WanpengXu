const int maxSize=50;
template <class T>
class Stack{
    public:
    Stack();
    virtual void Push(const T& s)=0;
    virtual bool Top(T& s)=0;
    virtual bool getTop(T& s)const=0;
    virtual bool IsEmpty()const=0;
    virtual bool IsFull()const=0;
    virtual int getSize()const=0;
};
