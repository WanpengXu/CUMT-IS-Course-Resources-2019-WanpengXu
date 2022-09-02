#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define LOCAL_PORT 4399

int main(int argc, char *argv[])
{
    int sockfd;
    struct sockaddr_in from_addr;                       /* 发送方地址信息 */
    struct sockaddr_in local_addr;                      /* 本机地址信息 */
    int from_len = sizeof from_addr;                    /* 地址结构体的长度 */
    int sz;                                             /* 接收到的数据长度 */
    char buf[128];                                      /* 接收数据缓冲区 */

    sockfd = socket(AF_INET, SOCK_DGRAM, 0);            /* 初始化一个IPv4族的数据报socket */
    if (sockfd == -1) {                                 /* 如果初始化socket失败 */
        perror("socket");
        exit(EXIT_FAILURE);
    }

    local_addr.sin_family = AF_INET;                    /* 协议族 */
    local_addr.sin_port = htons(LOCAL_PORT);            /* 本地端口 */
    local_addr.sin_addr.s_addr = htonl(INADDR_ANY);     /* 任意本地地址 */

    bind(sockfd, (struct sockaddr *)&local_addr, sizeof local_addr);     /* socket绑定 */

    sz = recvfrom(sockfd, buf, 128, 0, (struct sockaddr*)&from_addr, &from_len);    /* 接收数据 */
    if (sz == -1) {                                     /* 接收数据失败 */
        perror("recvfrom");
        exit(EXIT_FAILURE);
    }

    /* 数据处理 */

    exit(EXIT_SUCCESS);
}
