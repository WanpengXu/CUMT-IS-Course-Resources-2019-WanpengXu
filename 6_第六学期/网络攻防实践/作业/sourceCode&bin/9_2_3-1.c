#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main()
{
    char str[1 << 10];
    while (1)
    {
        memset(str, '\0', 1 <<  10);
        read(0, str, 1 << 10);
        printf(str);
        fflush(stdout);  // 将输出缓冲区内的数据打印到标准输出设备上
    }
}
