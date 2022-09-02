#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#define LOCAL_PORT 4399

int main(int argc, char *argv[])
{
    int sockfd;                                 /* 套接字文件描述符 */
    struct sockaddr_in to_addr;                 /* 接收方地址信息 */
    int to_len = sizeof to_addr;                /* 地址结构体的长度 */
    char buf[128];                              /* 发送数据缓冲区 */
    int sz;                                     /* 发送到的数据长度 */

    sockfd = socket(AF_INET, SOCK_DGRAM, 0);    /* 初始化一个IPv4族的数据报socket */
    if (sockfd == -1) {                         /* 初始化socket失败 */
        perror("socket");
        exit(EXIT_FAILURE);
    }

    to_addr.sin_family = AF_INET;            /* 协议族 */
    to_addr.sin_port = htons(LOCAL_PORT);    /* 本地端口 */
    to_addr.sin_addr.s_addr = inet_addr("192.168.1.1");       /* 将数据发送到192.168.1.1 */

    sz = sendto(sockfd, buf, 128, 0, (struct sockaddr *)&to_addr, to_len);    /* 发送数据 */
    if (sz == -1) {                             /* 接收数据失败 */
        perror("sendto");
        exit(EXIT_FAILURE);
    }

    /* 数据处理 */

    exit(EXIT_SUCCESS);
}
