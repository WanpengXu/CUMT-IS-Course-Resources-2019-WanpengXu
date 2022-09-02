#include "tlpi_hdr.h"
#include "curr_time.h"
#include <time.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
	// C将用到的变量前置定义，包括循环变量
    int numDead;  // 已终止的进程数
    pid_t childPid;  // wait到的进程ID
    int j;

    if (argc < 2 || strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0)
        usageErr("%s \033[1msleep-time...\n", argv[0]);

    setbuf(stdout, NULL);  // 禁用stdout的缓冲

	// 为每个参数创建一个子进程
    for (j = 1; j < argc; j ++ )
    {
        switch(fork())
        {
            case -1:
                errExit("fork");
			// 每个子进程sleep一会儿后_exit
            case 0:
                printf("[%s] child %d started with PID %ld, sleeping %s seconds\n",
                        currTime("%T"), j, (long)getpid(), argv[j]);
                sleep(getInt(argv[j], GN_NONNEG, "sleep-time"));
                _exit(EXIT_SUCCESS);
            default:
                break;
        }
    }

	// 父进程wait每个子进程
    numDead = 0;
    while (1)  // bool不是ANSI C的原生类型
    {
        childPid = wait(NULL);
        if (childPid == -1)
        {
            if (errno == ECHILD)
            {
                printf("No more children - bye!\n");
                exit(EXIT_SUCCESS);
            }
            else
                errExit("wait");
        }

        numDead ++ ;
        printf("[%s] wait() returned child PID %ld (numDead=%d)\n",
                currTime("%T"), (long)childPid, numDead);
    }
}
