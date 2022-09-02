#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	int l = 0xabcddcba;
	short s = l;
	char c = l;

	printf("宽度溢出\n");
	printf("l = 0x%x (%d bits)\n", l, sizeof(l) * 8);
	printf("s = 0x%x (%d bits)\n", s, sizeof(s) * 8);
	printf("c = 0x%x (%d bits)\n", c, sizeof(c) * 8);

	printf("整型提升\n");
	printf("s + c = 0x%x (%d bits)\n", s + c, sizeof(s + c) * 8);
	
	exit(EXIT_SUCCESS);
}
