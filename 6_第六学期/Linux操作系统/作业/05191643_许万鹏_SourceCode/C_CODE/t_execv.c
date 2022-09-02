#include "tlpi_hdr.h"

int main(int argc, char *argv[])
{
    char *argVec[10];

    printf("The value of USER and SHELL in the caller: \n%s\n%s\n", getenv("USER"), getenv("SHELL"));

    if (putenv("USER=wanpengxu") != 0) errExit("putenv");

    argVec[0] = "printenv";
    argVec[1] = "USER";
    argVec[2] = "SHELL";
    argVec[3] = NULL;

    printf("The value of USER and SHELL in the callee:\n");
    execv("/usr/bin/printenv", argVec);
	
    errExit("execl");
}
