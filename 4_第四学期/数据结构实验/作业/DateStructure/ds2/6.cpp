#include<cstdio>
 
int main(){
    int C;
    scanf("%d",&C);
    while(C--){
        int n,m;
        scanf("%d %d",&n,&m);
        if(n%(m+1))
            printf("first\n");
        else
            printf("second\n");
    }
    return 0;
}