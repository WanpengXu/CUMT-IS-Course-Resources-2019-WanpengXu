#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

int main(int argc, char *argv[])
{
	int fd = -1;
	ssize_t sz = -1;

	char buf[] = "I'm an undergraduate named WanpengXu from CUMT.";		/* 存放待写入数据 */
	char filename[] = "test.txt";

	/* 打开文件并打印成功与否 */
	fd = open(filename, O_RDWR);										/* 以可读可写模式打开文件 */
	if (fd == -1) printf("Open file %s failure, fd: %d\n", filename, fd);
	else printf("Open file %s success, fd: %d\n", filename, fd);

	sz = write(fd, buf, strlen(buf));									/* 将buf中的数据全部写入到fd指向的文件中 */
	printf("Write %d bytes to file %s\n", sz, filename);

	close(fd);															/* 关闭文件描述符 */

	exit(EXIT_SUCCESS);
}
