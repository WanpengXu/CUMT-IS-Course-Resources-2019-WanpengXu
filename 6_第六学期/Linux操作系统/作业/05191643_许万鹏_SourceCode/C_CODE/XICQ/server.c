#include "need.h"

struct user users[MAX_USER_NUM];

void delete_user_online(int index)
{
	int i;
	char buffer[BUFFER_SIZE];

	if (index < 0) return;

	users[index].fd = -1;
	sprintf(buffer, "%s 离开了聊天室\n", users[index].username);
	/* 通知所有用户：index用户离开了聊天室 */
	for (i = 0; i < MAX_USER_NUM; i++) {
		if (users[i].fd == -1) continue;
		write(users[i].fd, buffer, strlen(buffer));
	}

	return;
}

int add_user(int sc, struct protocol* msg)
{
	int i;
	int index = -1;
	char buffer[BUFFER_SIZE];

	/* 添加到在线用户列表 */
	for (i = 0; i < MAX_USER_NUM; i++)
		if (users[i].state == -1) {  /* 结构体未使用 */
			users[i].state = 1;
			strcpy(users[i].username, msg->username);
			strcpy(users[i].passwd, msg->data);
			//printf("regist %s to %d\n", msg->username, i);
			index = i;
			return index;
		}

	return -1;		/* 结构体数组满了 */
}

void broadcast(int index, struct protocol* msg)
{
	int i;
	char buffer[BUFFER_SIZE];

	sprintf(buffer, "%s(member): %s\n", users[index].username, msg->data);

	for (i = 0; i < MAX_USER_NUM; i++) {
		if ((users[i].fd == -1) || (i == index)) continue;  /* 跳过离线成员和自己 */
		write(users[i].fd, buffer, strlen(buffer));
	}
}

int find_target_user(char* username)
{
	int i;

	for (int i = 0; i < MAX_USER_NUM; i++) {
		if (users[i].state == -1) continue;
		if (strcmp(username, users[i].username) == 0) return i;
	}

	return -1;
}

int find_target_user_online(int sc, int* index, struct protocol* msg)
{
	int i;

	for (i = 0; i < MAX_USER_NUM; i++) {
		if (users[i].state == -1) continue;  /* 结构体未使用 */

		if ((strcmp(msg->username, users[i].username) == 0) && (strcmp(msg->data, users[i].passwd) == 0)) {
			if (users[i].fd == -1) {  /* 未建立socket，即user离线 */
				users[i].fd = sc;	/* 建立socket连接 */
				*index = i;
				return OP_OK;
			}
			else {  /* 已建立socket，即user在线 */
				printf("%s had login\n", users[i].username);
				return USER_LOGED;
			}
		}
	}

	return USERNAME_PWD_NMATCH;
}

void personal_message(int index, struct protocol* msg)
{
	int target_index;
	char buffer[BUFFER_SIZE];
	target_index = find_target_user(msg->username);

	if (target_index == -1) {
		sprintf(buffer, "User not found: %s\n", msg->username);
		write(users[index].fd, buffer, strlen(buffer));
	}
	else {
		sprintf(buffer, "%s 对你说：\n%s", users[index].username, msg->data);
		write(users[target_index].fd, buffer, strlen(buffer));
	}

	return;
}

void list_online_user(int index)
{
	int i;
	struct protocol msg;

	for (i = 0; i < MAX_USER_NUM; i++) {
		if (users[i].fd == -1) continue;

		memset(&msg, 0, sizeof msg);
		msg.command = ONLINE_USER;
		msg.state = ONLINE_USER_OK;
		strcpy(msg.username, users[i].username);
		strcpy(msg.data, users[i].username);

		printf("list users[%d].username = %s\n", i, users[i].username);

		write(users[index].fd, &msg, sizeof msg);
	}

	msg.command = ONLINE_USER;
	msg.state = ONLINE_USER_OVER;

	write(users[i].fd, &msg, sizeof msg);

	return;
}

void registe(int sc, int* index, struct protocol* msg)
{
	int target_index;
	char buffer[BUFFER_SIZE];
	struct protocol msg_back;	/* S -> C */

	msg_back.command = REGISTE;

	target_index = find_target_user(msg->username);

	if (target_index == -1) {
		*index = add_user(sc, msg);

		users[*index].state = 1;
		msg_back.state = OP_OK;

		printf("User %s registe to index %d success!\n", msg->username, *index);
		write(sc, &msg_back, sizeof msg_back);
	}
	else {
		msg_back.state = USERNAME_EXIST;
		printf("User %s exist!\n", msg->username);

		write(sc, &msg_back, sizeof msg_back);
	}

	return;
}

void login(int sc, int* index, struct protocol* msg)
{
	int i;
	int return_code;
	char buffer[BUFFER_SIZE];
	struct protocol msg_back;

	msg_back.command = LOGIN;

	return_code = find_target_user_online(sc, index, msg);
	msg_back.state = return_code;
	if (return_code != OP_OK) {		/* USER_LOGED or USERNAME_PWD_NMATCH */
		strcpy(buffer, "There is no this user!\n");
		printf("User %s login fail!\n", msg->username);

		write(sc, &msg_back, sizeof msg_back);
	}
	else {
		strcpy(msg_back.data, "Login success!\n");
		printf("User %s login success! his index = %d\n", msg->username, *index);

		write(users[*index].fd, &msg_back, sizeof msg_back);
	}

	/* 通知所有在线用户，user上线了 */
	sprintf(buffer, "%s 进入了聊天室！", users[*index].username);
	for (i = 0; i < MAX_USER_NUM; i++)
		if (users[i].fd != -1)
			write(users[i].fd, buffer, strlen(buffer));
}

int send_file(int index, struct protocol* msg)
{
	int i;

	/* 将文件数据报文转发至所有已连接的客户端 */
	for (i = 0; i < MAX_USER_NUM; i++) {
		if ((users[i].fd == -1) || (i == index)) continue;  /* 跳过离线成员和自己 */
		printf("Sending to %s, msg.state = 0x%x\n", users[i].username, msg->state);
		write(users[i].fd, msg, sizeof (struct protocol));	/* 这里可能也有问题 */
	}

	return 0;
}

void* process_conn(void* arg)
{
	int sockfd = *((int*)arg);		/* 先从void*转到int*，然后取值成为int */
	char buffer[BUFFER_SIZE];
	int sz;
	int i;

	int index = -1;

	struct protocol msg;

	free(arg);

	while (1)
	{
		sz = read(sockfd, &msg, sizeof msg);
		if (sz <= 0) {
			printf("%s offline\n", users[index].username);
			delete_user_online(index);
			close(sockfd);
			return NULL;
		}
		switch (msg.command) {
			case REGISTE:
				registe(sockfd, &index, &msg);
				break;
			case LOGIN:
				login(sockfd, &index, &msg);
				break;
			case BROADCAST:
				broadcast(index, &msg);
				break;
			case PERSONAL_MESSAGE:
				personal_message(index, &msg);
				break;
			case ONLINE_USER:
				list_online_user(index);
				break;
			case SEND_FILE:
				send_file(index, &msg);
				break;
			default:
				break;
		}
	}
}

int main(int argc, char* argv[])
{
	char buffer[BUFFER_SIZE];
	int ss, sc;
	struct sockaddr_in server_addr;
	struct sockaddr_in client_addr;

	int port;
	int return_code;
	pthread_t pid;
	int* arg;
	int i;

	if (argc < 2 || strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0) {
		printf("Usage:%s PORT\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	// 加个port值域校验
	port = atoi(argv[1]);
	if (port < 0) {
		printf("Usage:%s IP PORT\033[1m(>0)\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	ss = socket(AF_INET, SOCK_STREAM, 0);
	if (ss == -1) {
		perror("socket");
		exit(EXIT_FAILURE);
	}

	bzero(&server_addr, sizeof server_addr);
	server_addr.sin_family = AF_INET;
	server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
	server_addr.sin_port = htons(port);

	return_code = bind(ss, (struct sockaddr*)&server_addr, sizeof server_addr);
	if (return_code == -1) {
		perror("bind");
		exit(EXIT_FAILURE);
	}

	return_code = listen(ss, BACKLOG);
	if (return_code == -1) {
		perror("listen");
		exit(EXIT_FAILURE);
	}

	for (i = 0; i < 64; i++) {
		users[i].fd = -1;
		users[i].state = -1;
	}

	while (1) {
		int addr_len = sizeof(struct sockaddr);

		sc = accept(ss, (struct sockaddr*)&client_addr, &addr_len);
		if (sc == -1) continue;
		printf("client's IP:%s	PORT:%d\n", inet_ntoa(client_addr.sin_addr), client_addr.sin_port);

		arg = malloc(sizeof(int));
		*arg = sc;
		pthread_create(&pid, NULL, process_conn, (void*)arg);
	}
	close(ss);
	close(sc);
}