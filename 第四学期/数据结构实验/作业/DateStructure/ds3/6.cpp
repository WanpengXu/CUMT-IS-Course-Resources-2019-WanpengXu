#include<cstdio>
int n,sum,e[55][55],dis[55],book[55];
int inf = 0xffffff;
  
void prim()
{
    int i,j,k,min;
    for(i = 1; i <= n; i ++)
    {
        dis[i] = e[1][i];
        book[i] = 0;
    }
    dis[1] = 0;
    book[1] = 1;
    for(i = 1; i < n; i ++)
    {
        min = inf;
        for(j = 1; j <= n; j ++)
        {
            if(book[j] == 0 && dis[j] < min)
            {
                min = dis[j];
                k = j;
            }
        }
        book[k] = 1;
        sum += dis[k];
        for(j = 1; j <= n; j ++)
            if(book[j] == 0 && dis[j] > e[k][j])
                dis[j] = e[k][j];
    }
    return ;
}
int main()
{
    int i,j;
    while(scanf("%d",&n) != EOF)
    {
        sum = 0;
        for(i = 1; i <= n; i ++)
        {
            for(j = 1; j <= n; j ++)
            {
                scanf("%d",&e[i][j]);
                if(i != j && e[i][j] == 0 )
                    e[i][j] = inf;
            }
        }
        prim();
        printf("%d\n",sum);
    }
    return 0;
}
