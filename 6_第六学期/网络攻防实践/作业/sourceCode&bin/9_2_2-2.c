#include <stdio.h>

int main()
{
    int i;
    char str[] = "hello";
    printf("%s %n\n", str, &i);
    printf("%d\n", i);

    return 0;
}
