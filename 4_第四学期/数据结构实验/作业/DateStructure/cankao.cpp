#include "stdio.h"
#include "stdlib.h"
//节点
typedef struct List {
    int data;         	//数据域
    struct List *next;  //指针域
} List;
 
//尾插法构建链表作为初始数据
void TailCreatList(List *L)
{
    List *s, *r;//s用来指向新生成的节点。r始终指向L的终端节点。  
    r = L;      //r指向了头节点，当前的头节点是终端节点。 
    for (int i = 0; i < 6; i++) {
        s = (struct List*) malloc(sizeof(struct List));//为新节点s申请空间
        scanf("%d",&(s->data));
        r->next = s; //尾指针指向s
        r = s;       //让s变成尾指针
    }
    r->next = NULL; //元素已经全部装入链表L中的终端节点指针域为NULL，L建立完成 
}
 
void split(List *&headL, List *&headA,List *&headB)
{
	int count = 1;     //count来标识奇偶数
     List  *p = headL; //p指向headL的头节点
     List  *temp;      //用temp来暂时保存偶数序号的节点
	 headB->next = NULL;
     while(p->next != NULL)
     {
		  //当count能被2整除的时候，代表处理的是bi
          if(count % 2 == 0)
          {	  
			 /*
			  //尾插法代码
			  q->next = p->next;
              q = q->next;
		      p->next = p->next->next;
              q->next = NULL;
			 */
			  //偶数节点移到headB中，并且使用头插法来满足逆序要求。
 
			  temp = p->next->next;
			  p->next->next = headB->next;
			  headB->next = p->next;
			  p->next = temp;
 
          } 
		  //当count不能被2整除的时候，代表处理的是ai
		  else 
		  { //奇数节点留在HeadL中
              p = p->next;
          }
		  count++;
     }
	 headA = headL;
}
 
//打印单链表
void DisPlay(List *L) {
    List *p = L->next;
    while (p != NULL) {
        printf("%d ", p->data);
        p = p->next;
    }
    printf("\n");
}
 
 
int main() {
	//原始单链表
	List *origin = (struct List*) malloc(sizeof(struct List));
	//奇数单链表
	List *newHeadA = (List*) malloc(sizeof(List));
    //偶数单链表
	List *newHeadB = (List*) malloc(sizeof(List));
    TailCreatList(origin);
    DisPlay(origin);
    split(origin,newHeadA,newHeadB);
	DisPlay(newHeadB);
 
}
/*#include <iostream>
using namespace std;
 
typedef struct LNode
{
	int data;
	LNode *next;
}LNode,*LinkList;
 
//创建链表
int CreateList(LinkList &L,int n)
{
	LNode *p,*r;int i;
	L=new LNode;
	L->next=NULL;
	r=L;
	for(i=0;i<n;i++)
	{
		p=new LNode;
		cin>>p->data;
		p->next=NULL;r->next=p;
		r=p;
	}
	return 0;
}
 
 
 
//输出链表
void display(LinkList L)
{
	LNode *p;
	p=L->next;
	cout<<"(";
	while(p)
	{cout<<p->data<<" ";
	p=p->next;}
	cout<<")"<<endl;
}
 
//拆分
int SplitList_L(LinkList &LA,LinkList &LB,LinkList &LC)
{
    LNode *pa;LNode *pb;LNode *pc;
    pa=LA->next;pb=LB;pc=LC;
    while(pa)
    {
       if(pa->data<0)
        {
            pb->next=pa;
            pa=pa->next;
            pb=pb->next;
            pb->next=NULL;
        }
        else
        {
            pc->next=pa;
            pa=pa->next;
            pc=pc->next;
            pc->next=NULL;
        }
 
    }
}
 
 
 
int main()
{
	LinkList LA;LinkList LB;LinkList LC;int n;;
 
 
	cout<<"请输入需要创建单链表A的长度："<<endl;
	cin>>n;
	cout<<"请依次输入需要存入的数据(尾插法&&非零)："<<endl;
	CreateList (LA,n);
 
	cout<<"单链表A为：";
	display(LA);
 
	LB=new LNode;LC=new LNode;
	LB->next=NULL;LC->next=NULL;
 
	SplitList_L(LA,LB,LC);
	cout<<"分解后单链表B为：";
	display(LB);
	cout<<"分解后单链表C为：";
	display(LC);
 
	return 0;
}
 */