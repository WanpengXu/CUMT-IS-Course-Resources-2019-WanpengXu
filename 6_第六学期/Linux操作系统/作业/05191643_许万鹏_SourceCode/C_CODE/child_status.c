#include "tlpi_hdr.h"
#include "print_wait_status.h"  // 声明printWaitStatus()
#include <sys/wait.h>

int main(int argc, char *argv[])
{
	int status;
	pid_t childPid;
	
	if (argc > 1 && (strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0))
		usageErr("%s [exit-status]\n", argv[0]);
	
	switch(fork())
	{
		case -1:
			errExit("fork");
		// 子进程：以给定的status立即退出 或 循环等待信号。
		case 0:
			printf("Child started with PID = %ld\n", (long)getpid());
			if (argc > 1)  // 如果命令行中提供了status
				exit(getInt(argv[1], 0, "exit-status"));
			else  // 否则循环等待信号
				while (1) pause();
			exit(EXIT_FAILURE);
		// 父进程：重复等待子进程，直到它 退出 或 被信号终止。
		default:
			while (1)
			{
				childPid = waitpid(-1, &status, WUNTRACED
#ifdef WCONTINUED  // WCONTINUED标志自Linux2.6.10起被提供，这里是为了保证兼容性
												| WCONTINUED
#endif
				);
				if (childPid == -1)
					errExit("waitpid");
				// 以16进制打印status，以10进制分别打印其高字节和低字节
				printf("waitpid() returned: PID = %ld; status = 0x%04x (%d, %d)\n", 
						(long)childPid, (unsigned int)status, status >> 8, status & 0xff);
				printWaitStatus(NULL, status);
				
				if (WIFEXITED(status) || WIFSIGNALED(status))
					exit(EXIT_SUCCESS);
			}
	}
}
