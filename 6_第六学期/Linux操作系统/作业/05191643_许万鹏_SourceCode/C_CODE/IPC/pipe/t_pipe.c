#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[])
{
    int fd[2];  							/* 两个文件描述符 */
    pid_t pid;								/* 进程ID */
    char buffer[20];						/* 数据缓冲区 */
	int return_code;						/* 返回值 */

	return_code = pipe(fd);
    if(return_code == -1)  					/* 创建管道 */
        perror("pipe");
	
	pid = fork();
	switch(pid) {
		case -1:
			perror("fork");
			exit(EXIT_FAILURE);
		case 0:								/* 子进程 */
			close(fd[1]); 					/* 关闭写端 */
			read(fd[0], buffer, 20);
			printf("%s", buffer);
		default:							/* 父进程 */
			close(fd[0]); 					/* 关闭读端 */
			write(fd[1], argv[1], strlen(argv[1]));
	}
	exit(EXIT_SUCCESS);
}
