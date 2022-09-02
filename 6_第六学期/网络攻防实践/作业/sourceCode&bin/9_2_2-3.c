#include <stdio.h>

int main()
{
    int i;

    printf("%10u%n\n", 1, &i);
    printf("%d\n", i);

    printf("%.50u%n\n", 1, &i);
    printf("%d\n", i);

    printf("%0100u%n\n", 1, &i);
    printf("%d\n", i);

    printf("%0246267631d%n\n", 1, &i);
    printf("%#x\n", i);

    return 0;
}
