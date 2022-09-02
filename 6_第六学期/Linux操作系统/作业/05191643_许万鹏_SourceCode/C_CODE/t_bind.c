#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/un.h>
#include <sys/types.h>
#include <sys/socket.h>

#define MY_SOCK_PATH "/somepath"
int main(int argc, char *argv[])
{
    int sockfd;
    struct sockaddr_un addr;  /* AF_UNIX对应的结构体 */
    sockfd = socket(AF_UNIX, SOCK_STREAM, 0);  /* 初始化一个AF_UNIX族、流类型的socket */

    if (sockfd == -1)  /* 检查是否正常初始化socket */
    {
        perror("socket");
        exit(EXIT_FAILURE);
    }

    memset(&addr, 0, sizeof (struct sockaddr_un));  /* 将addr置0 */

    addr.sun_family = AF_UNIX;  /* 协议族为AF_UNIX */
    strncpy(addr.sun_path, MY_SOCK_PATH, sizeof addr.sun_path - 1);  /* 复制MY_SOCK_PATH到addr结构体的sun_path */

    if (bind(sockfd, (struct sockaddr *) &addr, sizeof (struct sockaddr_un)) == -1)  /* 绑定并判断是否成功 */
    {
        perror("bind");
        exit(EXIT_FAILURE);
    }
	
	/* 数据发送、接收、处理过程 */

    close(sockfd);  /* 关闭套接字文件描述符 */
}
