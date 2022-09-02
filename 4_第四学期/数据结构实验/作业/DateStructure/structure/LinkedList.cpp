#include <iostream>
using namespace std;
struct LinkNode{
    int data;
    LinkNode *link;
    LinkNode(LinkNode *ptr=NULL){
        link=ptr;
    }
    LinkNode(const int&item,LinkNode *ptr=NULL){
        data=item;
        link=ptr;
    }
};
class LinkedList{
public:
    LinkNode *first;
    LinkedList(){
        first=new LinkNode;
    }
    LinkedList(const int& x){
        first=new LinkNode(x);
    }
    
    bool insert(int& x){
        LinkNode *current=NULL;
        LinkNode 
    }
};