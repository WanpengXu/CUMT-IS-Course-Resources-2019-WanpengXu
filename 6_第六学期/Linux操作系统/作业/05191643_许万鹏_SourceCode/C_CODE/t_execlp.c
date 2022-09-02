#include "tlpi_hdr.h"
  
int main(int argc, char *argv[])
{
    if (argc != 2 || strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0)  // 当参数数量不正确或指明--help/-h时显示Usage
        usageErr("%s \033[1mPATHNAME\n", argv[0]);  // Esc[{attr1};...;{attrn}m是控制字符，用于控制终端中的字体格式

    execlp(argv[1], argv[1], "Hello, World!", (char *)NULL);  // 注意要有(char *)显式转换
    errExit("execlp");  // 只有在程序异常时才会执行到这里
}
