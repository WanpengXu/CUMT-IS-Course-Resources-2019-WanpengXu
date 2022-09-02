#include <stdio.h>

int main()
{
    int j = 0;
    printf("%080d%1$hhn%035d%1$hhn%0129d%1$hhn%04d%1$hhn\n", &j);
    printf("%#x\n", j);


    printf("%080d%1$hhn\n", &j);
    printf("%#x\n", j);
    

    printf("%035d%1$hhn\n", &j);
    printf("%#x\n", j);
    
    printf("%0129d%1$hhn\n", &j);
    printf("%#x\n", j);
    
    printf("%04d%1$hhn\n", &j);
    printf("%#x\n", j);

    return 0;
}
