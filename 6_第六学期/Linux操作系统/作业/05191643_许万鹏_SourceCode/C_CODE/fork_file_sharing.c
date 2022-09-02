#include <sys/stat.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int fd, flags;  // fd(file description)：文件描述符，flags：文件状态标志
    char template[] = "/tmp/testXXXXXX";  // mkstemp(char template[])要求以XXXXXX结尾

    setbuf(stdout, NULL);

	// 以下命令失败后都返回-1
	// 父进程使用mkstemp()打开一个临时文件
    fd = mkstemp(template);  // 创建后六位随机的唯一临时文件，成功返回文件描述符
    if (fd == -1) perror("mkstemp");
    printf("File offset before fork(): %lld\n",
            (long long)lseek(fd, 0, SEEK_CUR));  // 打印将seek从当前（CUR）seek向后移动0byte后的读写位置（打印CUR seek）

    flags = fcntl(fd, F_GETFL);  // GET fd的FL(AGS)
    if (flags == -1) perror("fcntl - F_GETFL");
    printf("O_APPEND flag before fork() is: %s\n",
            (flags & O_APPEND) ? "on" : "off");  // 若flags的O_APPEND位为1（append模式）则打印on，否则打印off

    switch(fork()) {  // fork出子进程
        case -1:
            perror("fork");

        case 0:  // 在子进程中改变文件的文件描述符fd和文件状态标志flags
            if (lseek(fd, 1000, SEEK_SET) == -1) perror("lseek");  // 将seek设置（SET）为1000

            flags = fcntl(fd, F_GETFL);
            if (flags == -1) perror("fcntl - F_GETFL");

            flags |= O_APPEND;  // 将flags的O_APPEND位置为1
            if (fcntl(fd, F_SETFL, flags) == -1) perror("fcntl - F_SETFL");  // 将fd的FL SET为flags
            _exit(EXIT_SUCCESS);  // 清除进程的内存空间及其在内核中的数据结构，停止进程

        default:  // 父进程获取文件描述符fd和文件状态标志flags
            if (wait(NULL) == -1) perror("wait");  // 阻塞该进程（父进程）直到其某个子进程被停止，成功则返回该子进程的pid
            printf("\nChild has exited\n\n");

            printf("File offset after fork() in parent: %lld\n",
                    (long long)lseek(fd, 0, SEEK_CUR));  // 读取当前seek

            flags = fcntl(fd, F_GETFL);  // GET fd's FL
            if (flags == -1) perror("fcntl - F_GETFL");

            printf("O_APPEND flag after fork() in parent is: %s\n",
                    (flags & O_APPEND) ? "on" : "off");  // 同前述
            exit(EXIT_SUCCESS);  // 刷新stdio缓冲，执行_exit()
    }
}
