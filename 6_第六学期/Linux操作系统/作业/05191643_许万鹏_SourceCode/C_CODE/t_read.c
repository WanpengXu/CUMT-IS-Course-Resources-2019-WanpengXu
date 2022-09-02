#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

int main(int argc, char *argv[])
{
    int i;
    int fd = -1;
    ssize_t sz = -1;

    char buf[10];                           /* 存放待读取数据 */
    char filename[] = "test.txt";

    /* 打开文件并打印成功与否 */
    fd = open(filename, O_RDONLY);          /* 以只读模式打开文件 */
    if (fd == -1) printf("Open file %s failure, fd: %d\n", filename, fd);
    else printf("Open file %s success, fd: %d\n", filename, fd);

    /* 循环读取数据，直到文件末尾（0）或失败（-1） */
    while (sz) {
        sz = read(fd, buf, 10);             /* 每次read 10 bytes数据 */
        if (sz == -1) {                     /* 读取数据失败 */
            close(fd);
            perror("read");
            exit(EXIT_FAILURE);
        }
        else {                              /* 读取数据成功 */
            if (sz > 0) {                   /* 若未到EOF，则打印读取到的数据 */
                printf("Read %2d bytes: ", sz);
                printf("\"");
                for (i = 0; i < sz; i ++ )
                    printf("%c", buf[i]);
                printf("\"\n");
            }
            else printf("Reach the end of file.\n");
        }
    }
    exit(EXIT_SUCCESS);
}
