#include "tlpi_hdr.h"

int main(int argc, char *argv[])
{
    char *argVec[10];
    char *envVec[] = { "GREET=salut", "UNIVERSITY=cumt", "BYE=adieu", NULL };

    if (argc != 2 || strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0)  // 当参数数量不正确或指明--help/-h时显示Usage
        usageErr("%s pathname\n", argv[0]);

    // 为新程序创建参数列表
    argVec[0] = strrchr(argv[1], '/');  // 从argv[1]获取basename
    if (argVec[0] != NULL) argVec[0]++;  // 若得到了argv[1]中最右'/'的下标（绝对路径或其简化），将argVec[0]指向其后的字符串
    else argVec[0] = argv[1];  // 若argv[1]中没有'/'（相对路径），直接将argVec[0]指向字符串argv[1]
    argVec[1] = "hello world";
    argVec[2] = "goodbye world";
    argVec[3] = NULL;  // 参数列表必须以空结尾

    // 执行argv[1]中指定的程序
    execve(argv[1], argVec, envVec);
    errExit("execve");  // 只有在程序异常时才会执行到这里
}

