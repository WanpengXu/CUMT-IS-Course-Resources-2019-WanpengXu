#include "tlpi_hdr.h"

extern char **environ;

int main(int argc, char *argv[])
{
    int j;
    char **ep;

	// 显示参数列表
    for (j = 0; j < argc; j++)
        printf("argv[%d] = %s\n", j, argv[j]);

	// 显示环境列表
    for (ep = environ; *ep != NULL; ep++)
        printf("environ: %s\n", *ep);

    exit(EXIT_SUCCESS);
}

