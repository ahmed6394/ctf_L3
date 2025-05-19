#include <stdio.h>
#include <unistd.h>

void main(int ac, char **av)
{
    char name[] = "rob";
    int secret_number = 42;
    char fmt_buf[256];
    read(0, fmt_buf, 255);
    printf(fmt_buf, 12);
}