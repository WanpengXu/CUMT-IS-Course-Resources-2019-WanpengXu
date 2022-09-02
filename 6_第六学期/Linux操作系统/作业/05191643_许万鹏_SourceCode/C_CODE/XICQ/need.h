#ifndef _NEED_H
#define _NEED_H

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#include <pthread.h>

#define SERVER_PORT 8888
#define BACKLOG 5

#define BUFFER_SIZE 1024

#define MAX_USER_NUM 64
struct user
{
	int fd;
	int state;  // registed or not
	char username[1 << 5];
	char passwd[1 << 5];
};

/* C/S 通信传递的信息，包括命令、状态、用户名、数据 */
#define DATA_SIZE 128
struct protocol {
	int command;
	int state;
	char username[32];
	char data[DATA_SIZE];
};
/* command */
#define BROADCAST			0x00000001
#define PERSONAL_MESSAGE	0x00000002
#define REGISTE				0x00000004
#define LOGIN				0x00000008
#define ONLINE_USER			0x00000010
#define LOGOUT				0x00000020
#define SEND_FILE				0x00000040
/* state */
#define OP_OK				0x10000001
#define ONLINE_USER_OK		0x10000002
#define ONLINE_USER_OVER	0x10000004
#define USERNAME_EXIST		0x10000008
#define USERNAME_PWD_NMATCH	0x10000010
#define USER_LOGED			0x10000020
#define	USER_NOT_REGIST		0x10000040
#define FILE_HEAD			0x10000080
#define FILE_CONTENT		0x10000100
#define FILE_TAIL			0x10000200

#endif