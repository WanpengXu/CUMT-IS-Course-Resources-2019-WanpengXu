#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/un.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#define DEST_IP "124.221.90.96"
#define DEST_PORT 23
int main(int argc, char *argv[])
{
    int ret = 0;
    int sockfd;                                 /* sockfd：连接的socket */
    struct sockaddr_in server_addr;             /* 服务器地址信息 */

    sockfd = socket(AF_INET, SOCK_STREAM, 0);   /* 初始化一个IPv4族的流式连接 */
    if (sockfd == -1) {                         /* 检查是否正常初始化socket */
        perror("socket");
        exit(EXIT_FAILURE);
    }

    server_addr.sin_family = AF_INET;           /* 协议族，IPv4，主机字节序 */
    server_addr.sin_port = htons(DEST_PORT);    /* 端口，short型，网络字节序 */
    server_addr.sin_addr.s_addr = inet_addr(DEST_IP);   /* 服务器IP地址 */
    bzero(&(server_addr.sin_zero), 8);          /* 将保留字段sin_zero置0 */

    ret = connect(sockfd, (struct sockaddr *)&server_addr, sizeof (struct sockaddr));     /* 连接服务器 */

    /* 发送、接收、处理数据 */

    close(sockfd);                              /* 关闭服务器连接 */
}
