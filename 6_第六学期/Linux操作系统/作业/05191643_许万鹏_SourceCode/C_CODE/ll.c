#include <grp.h>
#include <pwd.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <sys/types.h>

void ll(char*);
void get_statistic(char*);
char* uid_to_name(uid_t);
char* gid_to_name(gid_t);
void show_file_info(char*, struct stat*);
void mode_to_letters(int, char[]);

int return_code;

int main(int argc, char* argv[])
{
	if (argc == 1)								/* 如果只有一个参数，对其ll */
		ll(".");
	else {										/* 如果有多个参数，对每个参数ll */
		while (--argc) {
			printf("%s:\n", *++argv);
			chdir(*argv);						/* 切换到参数目录 */
			ll(*argv);
			chdir("");							/* 切换回当前工作目录 */
		}
	}
	return 0;
}


void ll(char* dirname)
{
	DIR* dir_ptr;
	struct dirent* direntp;

	dir_ptr = opendir(dirname);
	if (dir_ptr == NULL) {
		fprintf(stderr, "ls: cannot open %s\n", dirname);
		get_statistic(dirname);					/* 如果不是目录就当作文件来显示其属性 */
	}
	else {
		while ((direntp = readdir(dir_ptr)) != NULL)
			get_statistic(direntp->d_name);		/*逐个显示目录里文件信息*/
		closedir(dir_ptr);
	}
}

void get_statistic(char* filename)
{
	struct stat info;
	return_code = stat(filename, &info);
	if (return_code == -1) perror(filename);	/*获取文件信息失败*/
	else show_file_info(filename, &info);		/*显示文件信息*/
}

void show_file_info(char* filename, struct stat* info_p)
{
	char* uid_to_name(), * ctime(), * gid_to_name();
	void mode_to_letters();
	char modestr[11];

	mode_to_letters(info_p->st_mode, modestr);

	printf("%s", modestr);
	printf("%3d", (int)info_p->st_nlink);
	printf("%5s", uid_to_name(info_p->st_uid));
	printf("%5s", gid_to_name(info_p->st_gid));
	printf("%6ld", (long)info_p->st_size);
	printf(" %.12s", 4 + ctime(&info_p->st_mtime));
	if (access(filename, X_OK) != -1) printf(" \033[32m%s\33[0m\n", filename);
	else printf(" %s\n", filename);
}


void mode_to_letters(int mode, char str[])
{
	/* 初始化 */
	strcpy(str, "----------");

	/* 获取文件类型 */
	if (S_ISREG(mode)) str[0] = '-';
	if (S_ISLNK(mode)) str[0] = 'l';
	if (S_ISDIR(mode)) str[0] = 'd';
	if (S_ISCHR(mode)) str[0] = 'c';
	if (S_ISBLK(mode)) str[0] = 'b';
	if (S_ISFIFO(mode)) str[0] = 'f';
	if (S_ISSOCK(mode)) str[0] = 's';

	/* 获取owner权限 */
	if (mode & S_IRUSR) str[1] = 'r';
	if (mode & S_IWUSR) str[2] = 'w';
	if (mode & S_IXUSR) str[3] = 'x';

	/* 获取group权限 */
	if (mode & S_IRGRP) str[4] = 'r';
	if (mode & S_IWGRP) str[5] = 'w';
	if (mode & S_IXGRP) str[6] = 'x';

	/* 获取other权限 */
	if (mode & S_IROTH) str[7] = 'r';
	if (mode & S_IWOTH) str[8] = 'w';
	if (mode & S_IXOTH) str[9] = 'x';
}



char* uid_to_name(uid_t uid)
{
	struct passwd* getpwuid(), * passwd_ptr;
	static char numstr[10];

	passwd_ptr = getpwuid(uid);
	if (passwd_ptr == NULL) {
		sprintf(numstr, "%d", uid);
		return numstr;
	}
	else
		return passwd_ptr->pw_name;
}


char* gid_to_name(gid_t gid)
{
	struct group* getgrgid(), * group_ptr;
	static char numstr[10];

	group_ptr = getgrgid(gid);
	if (group_ptr == NULL) {
		sprintf(numstr, "%d", gid);
		return numstr;
	}
	else
		return group_ptr->gr_name;
}

