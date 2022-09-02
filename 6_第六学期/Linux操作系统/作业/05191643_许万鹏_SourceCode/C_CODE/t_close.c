#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int fd = 0;                             /* 文件描述符 */

    while (fd >= 0) {                       /* 循环打开文件直到失败 */
        fd = open("test.txt", O_RDONLY);    /* 以只读模式打开文件 */
        if (fd > 0) {                       /* 打开文件成功 */
            printf("fd: %d\n", fd);         /* 打印文件描述符 */
            /* close(fd); */                /* 关闭文件描述符 */
        }
        else {                              /* 打开文件失败 */
            perror("open");                 /* 打印错误 */
            exit(EXIT_SUCCESS);             /* 退出 */
        }
    }
}
