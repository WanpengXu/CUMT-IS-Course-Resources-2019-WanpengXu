#include <iostream>
using namespace std;
struct DblNode{
    int data;
    DblNode *lLink,*rLink;
    DblNode(DblNode *left=NULL,DblNode *right=NULL)
        :lLink(left),rLink(right){}
    DblNode(int value,DblNode *left=NULL,DblNode *right=NULL)
        :data(value),lLink(left),rLink(right){}
};
class DblList{
public:
    DblNode *first;
    DblList(int uniqueVal){
        first=new DblNode(uniqueVal);
        first->rLink=first->lLink=first;
    }
    int length(){
        int count=0;
        DblNode *current=first->rLink;//
        while(current!=first){
            current=current->rLink;
            count++;
        }
        return count;
    }
    DblNode* search(const int& x){
        DblNode *current=first->rLink;
        while(current->data!=x&&current!=first)
            current=current->rLink;
        if(current==first)
            return NULL;
        else
            return current;
    }
    DblNode* locate(int i,bool d){
        if(i==0||first->rLink==first)//因为是尾插法建立
            return first;
        DblNode *current;
        if(d==false)
            current=first->lLink;//
        else
            current=first->rLink;
        for(int j=0;j<i;j++){
            if(current==first)//
                break;
            if(d==false)
                current=current->lLink;
            else
                current=current->rLink;
        }
        if(current==first)
            return NULL;
        else
            return current;
    }
    bool insert(int i,const int& x,bool d){//
        DblNode *current=locate(i,d);
        if(current==NULL)
            return false;
        DblNode *newNode=new DblNode(x);
        if(d==false){
            newNode->lLink=current->lLink;
            current->lLink=newNode;
            newNode->lLink->rLink=newNode;
            newNode->rLink=current;
        }
        else{
            newNode->rLink=current->rLink;
            current->rLink=newNode;
            newNode->rLink->lLink=newNode;
            newNode->lLink=current;
        }
        return true;
    }
    bool remove(int i,int& x,bool d){
        DblNode *current=locate(i,d);
        if(current==NULL)
            return false;
        current->rLink->lLink=current->lLink;
        current->lLink->rLink=current->rLink;
        x=current->data;
        delete current;
        return true;
    }
};