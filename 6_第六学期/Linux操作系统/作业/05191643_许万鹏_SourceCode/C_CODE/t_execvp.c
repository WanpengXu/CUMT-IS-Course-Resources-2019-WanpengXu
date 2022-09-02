#include "tlpi_hdr.h"

int main(int argc, char *argv[])
{
    char *argVec[10];

    if (argc != 2 || strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0)
        usageErr("%s \033[1mPATHNAME\n", argv[0]);

    argVec[0] = strrchr(argv[1], '/');
    if (argVec[0] != NULL) argVec[0] ++ ;
    else argVec[0] = argv[1];
    argVec[1] = "Hello, World!";
    argVec[2] = NULL;

    execvp(argv[1], argVec);
    errExit("execvp");
}
