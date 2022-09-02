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
int main(int argc, char *argv[])
{
    int sockfd;
    struct sockaddr_in addr;  			        /* AF_INET对应的结构体 */

    sockfd = socket(AF_INET, SOCK_STREAM, 0);   /* 初始化一个AF_INET族、流类型的socket */
    if (sockfd == -1) {							/* 检查是否正常初始化socket */
        perror("socket");
        exit(EXIT_FAILURE);
    }

    addr.sin_family = AF_INET;  				/* 协议族为AF_INET */
    addr.sin_port = htons(MY_PORT);
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");  /* 将字符串的IP地址转为网络字节序的IP地址 */
    bzero(&(addr.sin_zero), 8);                 /* 将addr.sin_zero置0，等价于memset((&(addr.sin_zero), 0, 8); */

    if (bind(sockfd, (struct sockaddr *) &addr, sizeof (struct sockaddr_in)) == -1) {  /* 绑定并判断是否成功 */
        perror("bind");
        exit(EXIT_FAILURE);
    }
	
	/* 数据发送、接收、处理过程 */

    close(sockfd);  						    /* 关闭套接字文件描述符 */
}
