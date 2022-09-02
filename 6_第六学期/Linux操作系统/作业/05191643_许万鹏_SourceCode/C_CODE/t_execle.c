#include "tlpi_hdr.h"

int main(int argc, char *argv[])
{
    char *envVec[] = { "GREET=salut", "UNIVERSITY=cumt", "BYE=adieu", NULL };
    char *filename;

    if (argc != 2 || strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0)  // 当参数数量不正确或指明--help/-h时显示Usage
        usageErr("%s pathname\n", argv[0]);

    filename = strrchr(argv[1], '/');  // 从argv[1]获取basename
    if (filename != NULL) filename++;  // 若得到了argv[1]中最右'/'的下标，将filename指向其后的字符串
    else filename = argv[1];  // 若argv[1]中没有'/'，直接将filename指向字符串argv[1]

    // 执行argv[1]中指定的程序
    execle(argv[1], filename, "Hello, World!", (char *)NULL, envVec);
    errExit("execve");  // 只有在程序异常时才会执行到这里
}
