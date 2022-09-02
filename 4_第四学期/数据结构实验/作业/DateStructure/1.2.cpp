#include <iostream>
struct LinkNode {    
    int  data;		       
    LinkNode * link;          	
}; 
class List{
    private:
        LinkNode *first;
    public:
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
};