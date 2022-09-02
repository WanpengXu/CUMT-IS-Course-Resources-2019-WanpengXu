#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/un.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#define MY_PORT 4399                            /* 端口地址 */
#define BACKLOG 10                              /* 侦听队列长度 */
int main(int argc, char* argv[])
{
    int sockfd, client_fd;                      /* sockfd：侦听的socket，client_fd：连接方的socket值 */

    struct sockaddr_in server_addr;             /* 服务器（本机）地址信息 */
    struct sockaddr_in client_addr;             /* 客户端地址信息 */
    int addr_length;                            /* 保存网络地址长度量 */

    sockfd = socket(AF_INET, SOCK_STREAM, 0);   /* 初始化一个IPv4族的流式连接 */

    if (sockfd == -1) {                         /* 检查是否正常初始化socket */
        perror("socket");                       /* 打印错误信息 */
        exit(EXIT_FAILURE);                     /* 退出程序 */
    }

    server_addr.sin_family = AF_INET;            /* 协议族，IPv4，主机字节序 */
    server_addr.sin_port = htons(MY_PORT);       /* 端口，short型，网络字节序 */
    server_addr.sin_addr.s_addr = INADDR_ANY;    /* 自动获得IP地址，手动添加使用inet_addr("127.0.0.1") */
    bzero(&(server_addr.sin_zero), 8);           /* 将addr.sin_zero置0，等价于memset((&(addr.sin_zero), 0, 8); */
    if (bind(sockfd, (struct sockaddr*)&server_addr, sizeof (struct sockaddr)) == -1) {   /* 绑定端口地址并判断是否成功 */
        perror("bind");                         /* 打印错误信息 */
        exit(EXIT_FAILURE);                     /* 退出程序 */
    }
    if (listen(sockfd, BACKLOG) == -1) {        /* 设置侦听队列长度为BACKLOG，并判断是否成功 */
        perror("listen");                       /* 打印错误信息 */
        exit(EXIT_FAILURE);                     /* 退出程序 */
    }

    printf("TCPServer Waiting for client on port 4399...\n");

    addr_length = sizeof (struct sockaddr_in);   /* 地址长度 */
    client_fd = accept(sockfd, (struct sockaddr *)&client_addr, &addr_length);     /* 等待客户端连接，地址在client_addr中*/

    if (client_fd == -1) {                      /* accept()失败 */
        perror("accept");                       /* 打印错误信息 */
        exit(EXIT_FAILURE);                     /* 退出程序 */
    }

    /* 处理客户端连接过程 */

    close(client_fd);                         /* 关闭客户端连接 */

    /* 其他过程 */

    close(sockfd);                              /* 关闭服务器连接 */
}
