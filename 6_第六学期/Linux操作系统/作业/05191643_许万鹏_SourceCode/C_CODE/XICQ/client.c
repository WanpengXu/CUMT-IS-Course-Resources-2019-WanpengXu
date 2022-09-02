#include "need.h"

int sockfd;
struct sockaddr_in server_addr;
int addr_len = sizeof(struct sockaddr);

pthread_t pid;

int is_login = 0;	/* 0：未登录 1：登录 */

/* 这两个聊天涉及缓冲区，目前保持这样是最理想状态 */
void broadcast(int fd)
{
	struct protocol msg;

	msg.command = BROADCAST;

	printf("待发送消息（以`字符结束）：\n");
	scanf("%[^`]%*c", msg.data);

	write(fd, &msg, sizeof msg);

	return;
}

void personal_message(int fd)
{
	struct protocol msg;

	msg.command = PERSONAL_MESSAGE;

	printf("输入目标用户，按Enter，再输入内容（以`字符结束）：\n");
	scanf("%s\n%[^`]%*c", msg.username, msg.data);

	write(fd, &msg, sizeof msg);

	return;
}

/* 读取部分交给线程 */
void list_online_user(int fd)
{
	struct protocol msg;

	msg.command = ONLINE_USER;
	write(fd, &msg, sizeof msg);
	getchar();
	getchar();
}

int registe(int fd)
{
	struct protocol msg, msg_back;

	msg.command = REGISTE;

	printf("请输入昵称：");
	scanf("%s", msg.username);

	printf("请输入密码：");
	scanf("%s", msg.data);

	write(fd, &msg, sizeof msg);			/* C->S */

	read(fd, &msg_back, sizeof msg_back);	/* S->C */
	if (msg_back.state == USERNAME_EXIST) {
		printf("昵称已使用！\n");
		getchar();
		getchar();
		return 1;	/* 1：失败 */
	}
	else if (msg_back.state == OP_OK) {
		printf("注册成功！\n");
		getchar();
		getchar();
		return 0;	/* 0：成功 */
	}
}

int login(int fd)
{
	struct protocol msg, msg_back;

	msg.command = LOGIN;

	printf("请输入昵称：");
	scanf("%s", msg.username);

	printf("请输入密码：");
	scanf("%s", msg.data);

	write(fd, &msg, sizeof msg);

	read(fd, &msg_back, sizeof msg_back);
	if (msg_back.state != OP_OK) {
		printf("登录失败！请检查你的信息！\n");
		is_login = 0;
		getchar();
		getchar();
		return USERNAME_PWD_NMATCH;
	}
	else {
		printf("登录成功!\n");
		is_login = 1;
		getchar();
		getchar();
		return OP_OK;
	}
}

int logout(int fd)
{
	close(fd);
	is_login = 0;
}

int send_file(int fd)
{
	int sz = 0;

	struct protocol msg;

	msg.command = SEND_FILE;

	printf("请输入文件路径：\n");
	scanf("%s", msg.username);

	FILE* fp = fopen(msg.username, "r");
	if (fp == NULL) {
		printf("文件未找到！");
		return 1;		/* .... */
	}

	/* 开始标志（主要是为了让server读到这个报文然后转入send_file函数） */
	msg.state = FILE_HEAD;
	write(fd, &msg, sizeof msg);
	printf("开始发送文件...\n");

	while (1) {
		msg.state = FILE_CONTENT;
		sz = fread(msg.data, sizeof(char), DATA_SIZE, fp);
		if (sz <= 0) break;
		write(fd, &msg, sizeof msg);
		bzero(msg.data, DATA_SIZE);
	}

	/* 结束标志 */
	msg.state = FILE_TAIL;
	write(fd, &msg, sizeof msg);
	printf("文件发送成功！\n");
	getchar();
	getchar();
	fclose(fp);

	return 0;
}

void* process_conn(void* arg)						/* 线程：用于接收服务器数据 */
{
	char buffer[BUFFER_SIZE];						/* 数据缓冲区 */
	int sz;											/* 实际接收数据字节数 */

	struct protocol* msg;							/* 报文指针 */

	FILE* fp;										/* 文件指针 */

	while (1) {
		if (is_login == 0) continue;				/* 如果本客户端未登录，等待本客户端登录 */

		memset(buffer, 0, sizeof buffer);			/* 清空数据缓冲区 */
		sz = read(sockfd, buffer, sizeof buffer);	/* 接收sockfd中的数据到数据缓冲区 */
		if (sz == -1) {								/* 接收失败 */
			close(sockfd);
			return NULL;
		}

		printf("收到数据！\n");

		/* 按报文格式解析 */
		msg = (struct protocol*)buffer;				/* 将数据缓冲区转换为报文格式 */
		if (msg->command == ONLINE_USER) {			/* 如果command为ONLINE_USER */
			switch (msg->state)
			{
				case ONLINE_USER_OK:				/* 如果state为ONLINE_USER_OK（成功找到在线用户） */
					printf("%s\n", msg->data);		/* 打印它 */
					break;
				case ONLINE_USER_OVER:				/* 如果state为ONLINE_USER_OVER（已找出所有在线用户） */
					printf("\n");					/* 打印空行 */
					break;
				default:
					printf("未知状态！\n");
					break;
			}
			continue;								/* 结束对该报文的处理 */
		}

		else if (msg->command == SEND_FILE) {		/* 如果command为SEND_FILE */
			int data_len;

			printf("数据为文件数据报！msg.state = 0x%x\n", msg->state);
			switch (msg->state)
			{
				case FILE_HEAD:
					fp = fopen("recv", "w");
					printf("已打开文件句柄！\n");
					break;
				case FILE_CONTENT:
					printf("正在接收文件内容！\n");
					data_len = strlen(msg->data);
					sz = fwrite(msg->data, sizeof(char), data_len, fp);	/* 向文件指针写入数据 */
					if (sz < data_len)
						perror("fwrite");
					break;
				case FILE_TAIL:
					printf("文件传输完成，内容已保存至\"./recv\"!\n");
					fclose(fp);
					break;
				default:
					printf("未知状态！\n");
					break;
			}
		}

		/* 如果数据不是报文，那么加结束符作为字符串打印至屏幕 */
		buffer[sz] = '\0';
		printf("%s\n", buffer);
	}
}

int main(int argc, char* argv[])
{
	int op;
	int min_op, max_op;
	int return_code;
	int port;

	int* arg;

	struct protocol msg;
	char buffer[BUFFER_SIZE];

	if (argc < 3 || strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0) {
		printf("Usage:%s IP PORT\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	/* PORT检查 */
	port = atoi(argv[2]);
	if (port < 0) {
		printf("Usage:%s IP PORT\033[1m(>0)\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (sockfd == -1) {
		perror("socket");
		exit(EXIT_FAILURE);
	}

	bzero(&server_addr, sizeof server_addr);
	server_addr.sin_family = AF_INET;
	server_addr.sin_addr.s_addr = inet_addr(argv[1]);  /* 再看看这 */
	server_addr.sin_port = htons(port);

	inet_pton(AF_INET, argv[1], &server_addr.sin_addr);

	return_code = connect(sockfd, (struct sockaddr*)&server_addr, addr_len);
	if (return_code == -1) {
		perror("connect");
		exit(EXIT_FAILURE);
	}

	//arg = malloc(sizeof(int));
	//*arg = sockfd;
	//pthread_create(&pid, NULL, process_conn, (void*)arg);

	pthread_create(&pid, NULL, process_conn, NULL);		/* 客户端只处理一个线程，直接用全局变量sockfd，不传参了 */

	while (1) {
		system("clear");
		printf("======================================\n");
		if (is_login == 0) {
			printf("\t[1]\t注册\n");
			printf("\t[2]\t登录\n");
		}
		else if (is_login == 1) {
			printf("\t[3]\t群聊\n");
			printf("\t[4]\t私聊\n");
			printf("\t[5]\t在线列表\n");
			printf("\t[6]\t发送群文件\n");
		}
		printf("\t[0]\t退出\n");
		printf("======================================\n");

		fflush(stdin);
		scanf("%d", &op);
		/* 处理0选项 */
		if (op == 0) {
			logout(sockfd);
			exit(EXIT_SUCCESS);
		}
		if (is_login == 0) min_op = 1, max_op = 2;
		else if (is_login == 1) min_op = 3, max_op = 6;

		if (op < min_op || op > max_op) {
			printf("无效的选项，请重新输入！\n");
			continue;
		}
		/* 处理0外的选项 */
		switch (op) {
			case 1:
				registe(sockfd);
				break;
			case 2:
				login(sockfd);
				break;
			case 3:
				broadcast(sockfd);
				break;
			case 4:
				personal_message(sockfd);  /* private */
				break;
			case 5:
				list_online_user(sockfd);
				break;
			case 6:
				send_file(sockfd);
				break;
			default:
				break;
		}
	}
}