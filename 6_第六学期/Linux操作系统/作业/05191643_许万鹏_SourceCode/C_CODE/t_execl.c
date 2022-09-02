#include "tlpi_hdr.h"

int main(int argc, char *argv[])
{
    printf("The value of USER and SHELL in the caller: \n%s\n%s\n", getenv("USER"), getenv("SHELL"));  // 打印主调进程的两个环境变量

    if (putenv("USER=wanpengxu") != 0) errExit("putenv");  // 主调进程改变自己的环境变量USER

	// 打印被调进程的两个环境变量
    printf("The value of USER and SHELL in the callee:\n");
    execl("/usr/bin/printenv", "printenv", "USER", "SHELL", (char *)NULL);
	
    errExit("execl");  //   // 只有在程序异常时才会执行到这里
}
